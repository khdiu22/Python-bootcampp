from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('set-theme/', views.set_theme_view, name='set_theme'),
    path('add-to-cart/', views.add_to_cart_view, name='add_to_cart'),
    path('clear-cart/', views.clear_cart_view, name='clear_cart'),
]