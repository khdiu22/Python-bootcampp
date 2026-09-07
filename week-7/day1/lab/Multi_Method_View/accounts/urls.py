from django.urls import path
from .views import RegisterView, LoginView, ProfileView, status_endpoint, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('status/', status_endpoint, name='status'),
]