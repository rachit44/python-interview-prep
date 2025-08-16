# README.md
# Python Interview Preparation Platform

A comprehensive full-stack web application built with Django and FastAPI to help developers prepare for Python interviews with real code examples, practice questions, and detailed explanations.

## 🚀 Features

- **Comprehensive Topics**: Covers Python fundamentals, Django, FastAPI, databases, and system design
- **Interactive Code Examples**: Syntax-highlighted code with explanations and GitHub links
- **Interview Questions**: Real interview questions with detailed sample answers
- **Responsive Design**: Mobile-friendly interface built with Tailwind CSS
- **Category-based Organization**: Topics organized by difficulty and category
- **Search & Filter**: Find topics by category, difficulty, or keywords
- **RESTful API**: Full API access to all content with Django REST Framework
- **FastAPI Integration**: Separate FastAPI service with modern async examples

## 🛠️ Technology Stack

### Backend
- **Django 4.2**: Main web framework
- **Django REST Framework**: API development
- **FastAPI**: Modern async API examples
- **PostgreSQL**: Primary database
- **SQLite**: Development database

### Frontend
- **HTML5/CSS3**: Structure and styling
- **Tailwind CSS**: Utility-first CSS framework
- **JavaScript (ES6+)**: Interactive functionality
- **Prism.js**: Syntax highlighting
- **Font Awesome**: Icons

### DevOps
- **Docker & Docker Compose**: Containerization
- **Gunicorn**: WSGI server
- **Uvicorn**: ASGI server for FastAPI

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose (recommended)
- Git

## 🚀 Quick Start

### Using Docker (Recommended)

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/python-interview-prep.git
cd python-interview-prep
```

2. **Build and run with Docker Compose**
```bash
docker-compose up --build
```

3. **Access the application**
- Django app: http://localhost:8000
- FastAPI docs: http://localhost:8001/docs
- Admin panel: http://localhost:8000/admin

### Manual Setup

1. **Clone and setup virtual environment**
```bash
git clone https://github.com/yourusername/python-interview-prep.git
cd python-interview-prep
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Setup environment variables**
```bash
cp .env.example .env
# Edit .env with your settings
```

4. **Run migrations and load sample data**
```bash
python manage.py migrate
python manage.py load_sample_data
python manage.py createsuperuser
```

5. **Start the development server**
```bash
python manage.py runserver
```

6. **Start FastAPI server (separate terminal)**
```bash
cd apps/examples/fastapi_examples
uvicorn main:app --reload --port 8001
```

## 📚 Project Structure

```
python-interview-prep/
├── config/                 # Django configuration
├── apps/
│   ├── core/              # Core application logic
│   ├── topics/            # Topics, categories, code examples
│   └── examples/          # FastAPI and code examples
├── templates/             # HTML templates
├── static/               # CSS, JavaScript, images
├── media/                # User uploads
├── tests/                # Test files
├── requirements.txt      # Python dependencies
├── docker-compose.yml    # Docker configuration
└── README.md
```

## 🎯 Usage

### For Interview Preparation

1. **Browse Topics**: Start with featured topics or browse by category
2. **Study Code Examples**: Review real-world code with explanations
3. **Practice Questions**: Test your knowledge with interview questions
4. **Filter by Difficulty**: Progress from beginner to advanced topics

### For Contributors

1. **Add Topics**: Use Django admin to add new interview topics
2. **Create Code Examples**: Add practical code examples with explanations
3. **Write Questions**: Contribute interview questions with detailed answers

## 🔧 Development

### Adding New Topics

1. Access Django admin at `/admin/`
2. Create categories and topics
3. Add code examples and interview questions
4. Topics automatically appear on the frontend

### API Development

- Django REST API: `/api/`
- FastAPI examples: Port 8001
- API documentation: `/api/docs/` (Django) and `:8001/docs` (FastAPI)

### Running Tests

```bash
python manage.py test
```

## 📱 Mobile Responsiveness

The platform is fully responsive with:
- Mobile-first design approach
- Touch-friendly interfaces
- Optimized code viewing on small screens
- Collapsible navigation menu

## 🚀 Deployment

### Production Setup

1. **Environment Variables**
```bash
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=your-production-database-url
ALLOWED_HOSTS=yourdomain.com
```

2. **Database Migration**
```bash
python manage.py migrate
python manage.py collectstatic
```

3. **Web Server**
Use Gunicorn with Nginx in production:
```bash
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Your Name** - Initial work - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Django community for excellent documentation
- FastAPI team for modern Python API development
- Tailwind CSS for utility-first styling
- Prism.js for beautiful syntax highlighting

## 📞 Support

If you have any questions or issues:

1. Check the [Issues](https://github.com/yourusername/python-interview-prep/issues) page
2. Create a new issue with detailed description
3. Contact: your.email@example.com

---

**Happy Interview Preparation! 🐍✨**