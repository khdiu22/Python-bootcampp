# This is your project-level urls.py (usually mysite/urls.py).
# Include the app's urls.py here.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("courses.urls")),
]
