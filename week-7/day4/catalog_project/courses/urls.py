from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    # Step 2: list route
    path("courses/", views.course_list, name="course_list"),
    # Step 2: detail route with an int converter
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
]
