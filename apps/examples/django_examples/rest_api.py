# apps/examples/django_examples/rest_api.py
from datetime import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['GET'])
@permission_classes([AllowAny])
def api_overview(request):
    """
    Django REST Framework API Overview
    Demonstrates basic API structure and documentation
    """
    api_urls = {
        'Overview': '/api/',
        'User Registration': '/api/register/',
        'User Login': '/api/login/',
        'User Profile': '/api/profile/',
        'All Users': '/api/users/',
        'Health Check': '/api/health/',
    }
    return Response({
        'message': 'Django REST Framework API Examples',
        'endpoints': api_urls,
        'version': '1.0.0'
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    User Registration Endpoint
    Demonstrates POST request handling and validation
    """
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        # Validation
        if not all([username, email, password]):
            return Response({
                'error': 'Username, email, and password are required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if user exists
        if User.objects.filter(username=username).exists():
            return Response({
                'error': 'Username already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Create token
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'message': 'User created successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'token': token.key
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({
            'error': f'An error occurred: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """
    User Login Endpoint
    Demonstrates authentication and token generation
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({
            'error': 'Username and password are required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'token': token.key
        })
    else:
        return Response({
            'error': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_user_profile(request):
    """
    Get User Profile
    Demonstrates authenticated endpoints and user data access
    """
    user = request.user
    return Response({
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'date_joined': user.date_joined,
            'is_active': user.is_active,
        }
    })

@api_view(['GET'])
def health_check(request):
    """
    Health Check Endpoint
    Demonstrates simple status checking
    """
    return Response({
        'status': 'healthy',
        'message': 'Django REST API is running',
        'timestamp': timezone.now()
    })
