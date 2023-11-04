# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import User

class UserOperationsView(View):
    def get(self, request, pseudo):
        user = User.read_user(pseudo)
        if user:
            user_data = {
                'name': user.name,
                'firstname': user.firstname,
                'pseudo': user.pseudo,
            }
            return render(request, 'user_operations.html', {'user_data': user_data})
        else:
            return render(request, 'user_operations.html',
                          {'error_message': 'User not found', 'create_user': True})

    def post(self, request, pseudo):
        action = request.POST.get('action')
        if action == 'create':
            name = request.POST.get('name')
            firstname = request.POST.get('firstname')
            # Check if a user with the same username already exists
            if User.objects.filter(pseudo=pseudo).exists():
                return JsonResponse({'error': 'A user with the same username already exists.'})
            # Create a new user
            user = User.create_user(name, firstname, pseudo)
            if user:
                return JsonResponse({'success': 'User created successfully'})
            else:
                return JsonResponse({'error': 'Failed to create the user'})

        if action == 'delete':
            # DELETE request to delete a user
            if User.delete_user(pseudo):
                return JsonResponse({'success': 'User deleted successfully'})
            else:
                return JsonResponse({'error': 'Failed to delete the user'}, status=404)

        if action == 'update':
            name = request.POST.get('name')
            firstname = request.POST.get('firstname')
            pseudo = request.POST.get('pseudo')
            # PUT request to update a user
            if User.update_user(pseudo, name, firstname):
                return JsonResponse({'success': 'User updated successfully'})
            else:
                return JsonResponse({'error': 'Failed to update the user'}, status=404)
