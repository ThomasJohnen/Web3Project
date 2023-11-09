from django.db import models
from products.models import Product


class Wishlist(models.Model):
    wishlistId = models.IntegerField(primary_key=True)
    pseudo = models.CharField(max_length=200)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlists'

    @classmethod
    def add_product_to_wishlist(cls, pseudo, productId):
        try:
            product = Product.objects.get(pk=productId)
            wish_list = cls(pseudo=pseudo, productId=product)
            wish_list.save()
        except Product.DoesNotExist:
            # Gérer le cas où le produit n'existe pas
            print(f"Le produit avec l'ID {productId} n'existe pas.")

    @classmethod
    def delete_product_from_wishlist(cls, pseudo, productId):
        try:
            wish_list = cls.objects.get(pseudo=pseudo, product_id=productId)
            wish_list.delete()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def get_wishlist_pseudo(cls, pseudo):
        wishlists = cls.objects.filter(pseudo=pseudo)
        product_info = []
        for wishlist in wishlists:
            try:
                product = Product.objects.get(pk=wishlist.productId)
                product_info.append({
                    'name': product.name,
                    'category': product.category,
                    'price': product.price,
                })
            except Product.DoesNotExist:
                # Handle the case where the product doesn't exist
                pass
        return product_info

    @classmethod
    def get_wishlist_id(cls, wishlist_id):
        return cls.objects.get(wishlistId=wishlist_id)

    @classmethod
    def delete_wishlist(cls, pseudo):
        wishlists = cls.objects.filter(pseudo=pseudo)
        wishlists.delete()
        return True

    @classmethod
    def delete_product_from_wishlists(cls, productId):
        wishlists = cls.objects.filter(product_id=productId)
        wishlists.delete()
        return True
