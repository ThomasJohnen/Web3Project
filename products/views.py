from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

from django.contrib.auth.decorators import login_required


@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        product_data = request.POST
        created = Product.create_one(
            product_data['id'],
            product_data['name'],
            product_data['category'],
            product_data['price']
        )
        if created:
            return JsonResponse({'message': 'Product created successfully'}, status=201)
        return JsonResponse({'message': 'Product already exists'}, status=209)
    return JsonResponse({'message': 'Method not allowed'}, status=405)


@login_required
def get_all_products(request):
    if request.method == 'GET':
        products = Product.read_all()
        product_data = [{'id': product.id, 'name': product.name, 'category': product.category, 'price': product.price}
                        for product in products]
        return JsonResponse(product_data, safe=False, status=200)
    return JsonResponse({'message': 'Method not allowed'}, status=405)


def get_product(request, id):
    if request.method == 'GET':
        product = Product.read_one(id)
        if product:
            product_data = {'id': product.id, 'name': product.name, 'category': product.category, 'price': product.price}
            return JsonResponse(product_data, status=200)
        return JsonResponse({'message': 'Product not found'}, status=404)
    return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def update_product(request, id):
    if request.method == 'PUT':
        product_data = request.POST
        product = Product.read_one(id)
        if product:
            product.update(
                product_data['name'],
                product_data['category'],
                product_data['price']
            )
            return JsonResponse({'message': 'Product updated successfully'}, status=200)
        return JsonResponse({'message': 'Product not found'}, status=404)
    return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def delete_all_products(request):
    if request.method == 'DELETE':
        Product.delete_all()
        return JsonResponse({'message': 'All products are deleted'}, status=200)
    return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def delete_product(request, id):
    if request.method == 'DELETE':
        product = Product.read_one(id)
        if product:
            product.delete_one(id)
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        return JsonResponse({'message': 'Product not found'}, status=404)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
