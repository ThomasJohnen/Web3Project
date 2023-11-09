from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("create/", views.createWishlist, name='create_wishlist'),
    path("<int:wishlistId>/", views.detailId, name='detail_id'),
    path("<str:pseudo>/", views.detailPseudo, name='detail_pseudo'),
]
