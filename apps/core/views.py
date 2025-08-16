# apps/core/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from apps.topics.models import Category, Topic

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['featured_topics'] = Topic.objects.filter(is_featured=True)[:6]
        context['total_topics'] = Topic.objects.count()
        context['total_categories'] = Category.objects.count()
        return context

def api_stats(request):
    """API endpoint for dashboard statistics"""
    stats = {
        'total_topics': Topic.objects.count(),
        'total_categories': Category.objects.count(),
        'difficulty_breakdown': {
            'beginner': Topic.objects.filter(difficulty='beginner').count(),
            'intermediate': Topic.objects.filter(difficulty='intermediate').count(),
            'advanced': Topic.objects.filter(difficulty='advanced').count(),
        }
    }
    return JsonResponse(stats)
