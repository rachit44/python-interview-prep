# apps/topics/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TopicViewSet, TopicListView, TopicDetailView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'topics', TopicViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', TopicListView.as_view(), name='topic_list'),
    path('<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
]