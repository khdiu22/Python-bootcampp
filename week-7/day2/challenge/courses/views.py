from django.http import Http404
from django.shortcuts import render

# NOTE: This uses a plain Python list instead of a database model,
# matching what the lab slide asks for (a list of courses passed in context).
COURSES = [
    {
        "id": 1,
        "name": "python for beginners",
        "level": "Beginner",
        "student_count": 32,
        "description": (
            "<strong>Learn Python</strong> from scratch with hands-on exercises "
            "and small projects. This description is trusted and contains safe HTML."
        ),
        "image": "python.jpg",
        "trusted": True,
    },
    {
        "id": 2,
        "name": "django web development",
        "level": "Intermediate",
        "student_count": 18,
        "description": (
            "Build full websites with Django: models, views, templates, and "
            "the admin panel, then deploy your project to the web."
        ),
        "image": "django.jpg",
        "trusted": False,
    },
    {
        "id": 3,
        "name": "data structures and algorithms",
        "level": "Advanced",
        "student_count": 0,
        "description": (
            "A deep dive into stacks, queues, trees, graphs, and the algorithms "
            "that run on them, with a focus on efficiency and problem solving."
        ),
        "image": "dsa.jpg",
        "trusted": False,
    },
    {
        "id": 4,
        "name": "web design with html and css",
        "level": "Beginner",
        "student_count": 40,
        "description": (
            "Design clean, responsive web pages using modern HTML and CSS, "
            "covering layout, typography, and basic animation."
        ),
        "image": "webdesign.jpg",
        "trusted": False,
    },
    {
        "id": 5,
        "name": "database systems",
        "level": "Intermediate",
        "student_count": 22,
        "description": (
            "Understand relational databases, SQL queries, and how to design "
            "schemas that scale for real applications."
        ),
        "image": "database.jpg",
        "trusted": False,
    },
]


def home(request):
    return render(request, "courses/home.html", {"username": "To US"})


def courses(request):
    return render(request, "courses/courses.html", {
        "username": "To US",
        "courses": COURSES,
    })


def course_detail(request, course_id):
    course = next((c for c in COURSES if c["id"] == course_id), None)

    if course is None:
        raise Http404("Course not found")

    return render(request, "courses/course_detail.html", {"course": course})
