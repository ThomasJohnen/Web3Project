from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('list/', views.get_all_products, name='list_products'),
    path('<str:id>/', views.get_product, name='get_product'),
    path('<str:id>/update/', views.update_product, name='update_product'),
    path('delete/', views.delete_all_products, name='delete_all_products'),
    path('<str:id>/delete/', views.delete_product, name='delete_product'),
]
