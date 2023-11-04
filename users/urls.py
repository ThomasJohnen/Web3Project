from django.urls import path

from users.views import UserOperationsView

urlpatterns = [
    path("<str:pseudo>/", UserOperationsView.as_view(), name='user_operations')
    ]