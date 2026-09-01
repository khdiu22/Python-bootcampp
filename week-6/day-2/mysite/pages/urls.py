from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq', views.index, name='faq'),
    path('team', views.team, name='team'),
]