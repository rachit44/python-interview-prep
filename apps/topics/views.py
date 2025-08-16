# apps/topics/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Topic, CodeExample
from .serializers import CategorySerializer, TopicSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def topics(self, request, pk=None):
        category = self.get_object()
        topics = category.topics.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.select_related('category').prefetch_related('code_examples', 'interview_questions')
    serializer_class = TopicSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'tags']
    ordering_fields = ['created_at', 'title', 'difficulty']

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_topics = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(featured_topics, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        difficulty = request.query_params.get('level', 'intermediate')
        topics = self.queryset.filter(difficulty=difficulty)
        serializer = self.get_serializer(topics, many=True)
        return Response(serializer.data)
    
# Django Template Views
class TopicListView(ListView):
    model = Topic
    template_name = 'topics/topic_list.html'
    context_object_name = 'topics'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        context['selected_difficulty'] = self.request.GET.get('difficulty')
        return context

    def get_queryset(self):
        queryset = Topic.objects.select_related('category')
        category = self.request.GET.get('category')
        difficulty = self.request.GET.get('difficulty')
        
        if category:
            queryset = queryset.filter(category__id=category)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
            
        return queryset

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topics/topic_detail.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['code_examples'] = self.object.code_examples.all()
        context['interview_questions'] = self.object.interview_questions.all()
        return context
