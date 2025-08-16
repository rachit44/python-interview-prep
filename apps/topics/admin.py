
# apps/topics/admin.py
from django.contrib import admin
from .models import Category, Topic, CodeExample, InterviewQuestion

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic_count', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('name', 'description')
    ordering = ('order', 'name')
    
    def topic_count(self, obj):
        return obj.topics.count()
    topic_count.short_description = 'Topics'

class CodeExampleInline(admin.TabularInline):
    model = CodeExample
    extra = 1
    fields = ('title', 'language', 'order')

class InterviewQuestionInline(admin.TabularInline):
    model = InterviewQuestion
    extra = 1
    fields = ('question', 'difficulty', 'order')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'is_featured', 'estimated_time', 'created_at')
    list_filter = ('category', 'difficulty', 'is_featured', 'created_at')
    search_fields = ('title', 'description', 'tags')
    list_editable = ('is_featured', 'difficulty')
    ordering = ('category__order', 'order', 'title')
    inlines = [CodeExampleInline, InterviewQuestionInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Metadata', {
            'fields': ('difficulty', 'estimated_time', 'tags', 'is_featured', 'order')
        }),
    )

@admin.register(CodeExample)
class CodeExampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'language', 'has_github_url', 'order')
    list_filter = ('language', 'topic__category', 'created_at')
    search_fields = ('title', 'description', 'code')
    ordering = ('topic', 'order', 'title')
    
    def has_github_url(self, obj):
        return bool(obj.github_url)
    has_github_url.boolean = True
    has_github_url.short_description = 'GitHub Link'

@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_preview', 'topic', 'difficulty', 'has_tips', 'order')
    list_filter = ('difficulty', 'topic__category', 'created_at')
    search_fields = ('question', 'sample_answer', 'tips')
    ordering = ('topic', 'order')
    
    def question_preview(self, obj):
        return obj.question[:80] + "..." if len(obj.question) > 80 else obj.question
    question_preview.short_description = 'Question'
    
    def has_tips(self, obj):
        return bool(obj.tips)
    has_tips.boolean = True
    has_tips.short_description = 'Has Tips'

# Custom admin site configuration
admin.site.site_header = "Python Interview Prep Admin"
admin.site.site_title = "Interview Prep Admin"
admin.site.index_title = "Welcome to Interview Prep Administration"