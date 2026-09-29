from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("products/active/", views.active_products),
    path("products/search/", views.search_products),
    path("products/create/", views.create_products),
    path("products/delete-inactive/", views.delete_inactive_products),
    path("products/<int:pk>/", views.product_detail),
    path("products/<int:pk>/update/", views.update_product_price),
    path("categories/<str:category>/deactivate/", views.deactivate_category),
]