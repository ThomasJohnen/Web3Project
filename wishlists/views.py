from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from .models import Wishlist


def index(request):
    wishlists = Wishlist.objects.all()
    context = {
        'wishlists': wishlists
    }

    return render(request, "wishLists/index.html", context)


def detailId(request, wishlistId):
    wishlist = Wishlist.get_wishlist_id(wishlistId)
    # wishlist = get_object_or_404(Wishlist, wishlistId=wishlistId)
    return render(request, "wishlists/detailId.html", {"wishlist": wishlist})



def detailPseudo(request, pseudo):
    wishlists = get_list_or_404(Wishlist.objects.filter(pseudo=pseudo).order_by('wishlistId')[:10])

    context = {
        'pseudo': pseudo,
        'wishlists': wishlists,
    }

    return render(request, "wishLists/detailPseudo.html", context)


def createWishlist(request):
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo')
        productId = request.POST.get('productId')

        if pseudo and productId:
            Wishlist.add_product_to_wishlist(pseudo, productId)
            return redirect('index')

    return render(request, 'wishLists/createWishlist.html')
