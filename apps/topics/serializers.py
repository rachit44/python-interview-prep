# apps/topics/serializers.py
from rest_framework import serializers
from .models import Category, Topic, CodeExample, InterviewQuestion

class CodeExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeExample
        fields = ['id', 'title', 'description', 'language', 'code', 'explanation', 'github_url']

class InterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestion
        fields = ['id', 'question', 'sample_answer', 'tips', 'difficulty']

class TopicSerializer(serializers.ModelSerializer):
    code_examples = CodeExampleSerializer(many=True, read_only=True)
    interview_questions = InterviewQuestionSerializer(many=True, read_only=True)
    tags_list = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = [
            'id', 'title', 'description', 'difficulty', 'estimated_time', 
            'tags', 'tags_list', 'is_featured', 'code_examples', 'interview_questions'
        ]

    def get_tags_list(self, obj):
        return obj.get_tags_list()

class CategorySerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)
    topic_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon', 'color', 'topics', 'topic_count']

    def get_topic_count(self, obj):
        return obj.topics.count()
