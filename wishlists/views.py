from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Wishlist


def index(request):
    wishlists = Wishlist.objects.all();
    context = {
        'wishlists': wishlists
    }

    return render(request, "wishLists/index.html", context)


def detailId(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id)
    return render(request, "wishLists/detailId.html", {"wishlist": wishlist})


def detailPseudo(request, pseudo):
    wishlists = get_list_or_404(Wishlist.objects.filter(pseudo=pseudo).order_by('wishlistId')[:10])

    context = {
        'pseudo': pseudo,
        'wishlists': wishlists,
    }

    return render(request, "WishLists/detailPseudo.html", context)
