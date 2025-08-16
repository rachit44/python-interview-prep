# apps/topics/management/commands/load_sample_data.py
import os
from django.core.management.base import BaseCommand
from apps.topics.models import Category, Topic, CodeExample, InterviewQuestion

class Command(BaseCommand):
    help = 'Load sample data for interview preparation'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')
        
        # Create Categories
        categories_data = [
            {
                'name': 'Python Fundamentals',
                'description': 'Core Python concepts, OOP, data structures, and algorithms',
                'icon': 'python',
                'color': '#3776ab',
                'order': 1
            },
            {
                'name': 'Django Framework',
                'description': 'Django web framework, models, views, templates, and REST API',
                'icon': 'globe',
                'color': '#092e20',
                'order': 2
            },
            {
                'name': 'FastAPI',
                'description': 'Modern, fast web framework for building APIs with Python',
                'icon': 'rocket',
                'color': '#009688',
                'order': 3
            },
            {
                'name': 'Database & ORM',
                'description': 'Database design, SQL, Django ORM, and query optimization',
                'icon': 'database',
                'color': '#336791',
                'order': 4
            },
            {
                'name': 'System Design',
                'description': 'Architecture patterns, scalability, and distributed systems',
                'icon': 'project-diagram',
                'color': '#6366f1',
                'order': 5
            }
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create Topics
        python_fundamentals = Category.objects.get(name='Python Fundamentals')
        django_category = Category.objects.get(name='Django Framework')
        fastapi_category = Category.objects.get(name='FastAPI')

        topics_data = [
            {
                'title': 'Python Data Structures & Algorithms',
                'description': 'Understanding lists, dictionaries, sets, and algorithmic thinking for interviews',
                'category': python_fundamentals,
                'difficulty': 'intermediate',
                'estimated_time': '45 minutes',
                'tags': 'data-structures, algorithms, lists, dictionaries',
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Object-Oriented Programming in Python',
                'description': 'Classes, inheritance, polymorphism, and design patterns commonly asked in interviews',
                'category': python_fundamentals,
                'difficulty': 'intermediate',
                'estimated_time': '60 minutes',
                'tags': 'oop, classes, inheritance, design-patterns',
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'Django REST API Development',
                'description': 'Building RESTful APIs with Django REST Framework, serializers, and viewsets',
                'category': django_category,
                'difficulty': 'intermediate',
                'estimated_time': '90 minutes',
                'tags': 'django-rest, api, serializers, viewsets',
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'FastAPI Async Operations',
                'description': 'Understanding async/await, dependency injection, and performance optimization',
                'category': fastapi_category,
                'difficulty': 'advanced',
                'estimated_time': '75 minutes',
                'tags': 'fastapi, async, performance, dependency-injection',
                'is_featured': True,
                'order': 1
            },
        ]

        for topic_data in topics_data:
            topic, created = Topic.objects.get_or_create(
                title=topic_data['title'],
                defaults=topic_data
            )
            if created:
                self.stdout.write(f'Created topic: {topic.title}')

        # Create Code Examples
        python_ds_topic = Topic.objects.get(title='Python Data Structures & Algorithms')
        
        code_examples = [
            {
                'topic': python_ds_topic,
                'title': 'List Comprehension vs Traditional Loops',
                'description': 'Performance comparison between list comprehensions and traditional loops',
                'language': 'python',
                'code': '''# Traditional loop approach
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i ** 2)

# List comprehension approach
result = [i ** 2 for i in range(10) if i % 2 == 0]

# Generator expression for memory efficiency
result_gen = (i ** 2 for i in range(10) if i % 2 == 0)

# Timing comparison
import timeit

def traditional_loop():
    result = []
    for i in range(1000):
        if i % 2 == 0:
            result.append(i ** 2)
    return result

def list_comp():
    return [i ** 2 for i in range(1000) if i % 2 == 0]

print("Traditional loop:", timeit.timeit(traditional_loop, number=1000))
print("List comprehension:", timeit.timeit(list_comp, number=1000))''',
                'explanation': 'List comprehensions are generally faster and more Pythonic. They create the entire list in memory, while generator expressions are memory-efficient for large datasets.',
                'order': 1
            },
            {
                'topic': python_ds_topic,
                'title': 'Dictionary Operations and Hash Tables',
                'description': 'Understanding dictionary internals and common interview patterns',
                'language': 'python',
                'code': '''# Dictionary creation and access patterns
user_data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

# Safe access with get() method
age = user_data.get('age', 0)  # Returns 0 if 'age' doesn't exist

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}

# Merging dictionaries (Python 3.9+)
default_config = {'debug': False, 'timeout': 30}
user_config = {'debug': True}
final_config = default_config | user_config

# Counter pattern for frequency counting
from collections import Counter
text = "hello world"
char_count = Counter(text)
print(char_count)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Two-sum problem using dictionary
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []''',
                'explanation': 'Dictionaries in Python are implemented as hash tables with O(1) average case lookup time. The two-sum solution demonstrates a common interview pattern using dictionaries for efficient lookups.',
                'order': 2
            }
        ]

        for example_data in code_examples:
            example, created = CodeExample.objects.get_or_create(
                title=example_data['title'],
                topic=example_data['topic'],
                defaults=example_data
            )
            if created:
                self.stdout.write(f'Created code example: {example.title}')

        # Create Interview Questions
        interview_questions = [
            {
                'topic': python_ds_topic,
                'question': 'Explain the difference between lists and tuples in Python. When would you use each?',
                'sample_answer': '''Lists and tuples are both sequence types in Python, but they have key differences:

**Lists:**
- Mutable (can be modified after creation)
- Use square brackets: [1, 2, 3]
- Support item assignment, append, remove, etc.
- Slightly more memory overhead
- Use when you need to modify the collection

**Tuples:**
- Immutable (cannot be modified after creation)
- Use parentheses: (1, 2, 3)
- Cannot be modified, but can be used as dictionary keys
- More memory efficient
- Use for fixed collections, coordinates, database records

**When to use:**
- Lists: Shopping cart items, user input collection, any dynamic data
- Tuples: Coordinates (x, y), database records, function returns with multiple values, dictionary keys when you need a composite key''',
                'tips': 'Mention performance implications and use cases. Interviewers often follow up with questions about dictionary keys and hashability.',
                'difficulty': 'beginner',
                'order': 1
            },
            {
                'topic': python_ds_topic,
                'question': 'How would you find the most frequent element in a list? Provide multiple approaches.',
                'sample_answer': '''I can think of several approaches, each with different time/space complexity:

**Approach 1: Using Counter (Most Pythonic)**
```python
from collections import Counter
def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]
```

**Approach 2: Using Dictionary**
```python
def most_frequent(lst):
    count = {}
    for item in lst:
        count[item] = count.get(item, 0) + 1
    return max(count, key=count.get)
```

**Approach 3: Using defaultdict**
```python
from collections import defaultdict
def most_frequent(lst):
    count = defaultdict(int)
    for item in lst:
        count[item] += 1
    return max(count, key=count.get)
```

**Time Complexity:** O(n) for all approaches
**Space Complexity:** O(k) where k is the number of unique elements

The Counter approach is most readable and handles edge cases well.''',
                'tips': 'Be ready to discuss time/space complexity and ask about edge cases like empty lists or ties between elements.',
                'difficulty': 'intermediate',
                'order': 2
            }
        ]

        for question_data in interview_questions:
            question, created = InterviewQuestion.objects.get_or_create(
                question=question_data['question'],
                topic=question_data['topic'],
                defaults=question_data
            )
            if created:
                self.stdout.write(f'Created interview question: {question.question[:50]}...')

        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data!')
        )