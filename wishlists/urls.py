from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:pseudo>/", views.detailPseudo, name='detail_pseudo'),
    path("<int:wishlist_id>/", views.detailId, name='detail_id')
]