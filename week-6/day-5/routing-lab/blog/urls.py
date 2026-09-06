from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]