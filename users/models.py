from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    pseudo = models.CharField(max_length=200)

    @classmethod
    def create_user(cls, name, firstname, pseudo):
        # Check if a user with the same nickname already exists
        if cls.objects.filter(pseudo=pseudo).exists():
            return None  # A user with the same nickname already exists, returns None
        # if the user does not exist, create it
        # Create a new user
        user = cls(name=name, firstname=firstname, pseudo=pseudo)
        user.save()
        return user

    @classmethod
    def delete_user(cls, pseudo):
        # Check if a user with the same nickname already exists
        if cls.objects.filter(pseudo=pseudo).exists():
            cls.objects.filter(pseudo=pseudo).delete()
            return True
        else:
            return False

    @classmethod
    def update_user(cls, pseudo, name, firstname):
        # Check if a user with the same nickname already exists
        if cls.objects.filter(pseudo=pseudo).exists():
            # Use the object manager on the class to perform the update
            cls.objects.filter(pseudo=pseudo).update(name=name, firstname=firstname)
            return True
        else:
            return False

    @classmethod
    def read_user(cls, pseudo):
        # Check if a user with the same nickname already exists
        if cls.objects.filter(pseudo=pseudo).exists():
            # Use the object manager on the class to retrieve the user
            user = cls.objects.get(pseudo=pseudo)
            return user
        else:
            return None
