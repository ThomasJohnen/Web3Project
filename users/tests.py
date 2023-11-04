from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
    def test_create_user(self):
        # Créez un utilisateur avec un pseudo qui n'existe pas encore
        user = User.create_user(name="Doe", firstname="John", pseudo="johndoe")

        # Vérifiez que l'utilisateur a été créé
        self.assertIsNotNone(user)

        # Vérifiez que l'utilisateur peut être récupéré de la base de données
        saved_user = User.objects.get(pseudo="johndoe")
        self.assertEqual(saved_user, user)

    def test_create_user_with_existing_pseudo(self):
        # Créez un utilisateur avec un pseudo qui existe déjà
        existing_user = User.create_user(name="Smith", firstname="Jane", pseudo="janesmith")
        self.assertIsNotNone(existing_user)

        user = User.create_user(name="Doe", firstname="John", pseudo="janesmith")

        # Vérifiez que l'utilisateur n'a pas été créé (doit renvoyer None)
        self.assertIsNone(user)

    def test_create_user_with_same_pseudo(self):
        # Créez deux utilisateurs avec le même pseudo
        user1 = User.create_user(name="Doe", firstname="John", pseudo="johndoe")
        user2 = User.create_user(name="Smith", firstname="Jane", pseudo="johndoe")

        # Vérifiez que le premier utilisateur est créé
        self.assertIsNotNone(user1)

        # Vérifiez que le deuxième utilisateur n'est pas créé (doit renvoyer un message d'erreur)
        self.assertIsNone(user2, "Un utilisateur avec le même pseudo existe déjà.")

    def test_delete_user(self):
        # Créez un utilisateur
        user = User.create_user(name="Van Bellinghen", firstname="Brandon", pseudo="Zenthor")

        # Vérifiez que l'utilisateur a été créé
        self.assertIsNotNone(user)

        # Supprimez l'utilisateur en utilisant la méthode d'instance
        deleted = user.delete_user(pseudo="Zenthor")

        # Vérifiez que l'utilisateur a été supprimé
        self.assertTrue(deleted)

        # Vérifiez que l'utilisateur n'existe plus dans la base de données
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pseudo="Zenthor")

    def test_delete_non_existing_user(self):
        # Tentez de supprimer un utilisateur qui n'existe pas
        deleted = User.delete_user(pseudo="nonexistentuser")

        # Vérifiez que la suppression renvoie False
        self.assertFalse(deleted)

    def test_update_existing_user(self):
        # Créez un utilisateur
        user = User.create_user(name="Doe", firstname="John", pseudo="johndoe")

        # Vérifiez que l'utilisateur a été créé
        self.assertIsNotNone(user)

        # Mettez à jour l'utilisateur en utilisant la méthode de classe
        updated = User.update_user(pseudo="johndoe", name="Updated", firstname="NewFirstName")

        # Vérifiez que l'utilisateur a été mis à jour avec succès
        self.assertTrue(updated)

        # Vérifiez que les attributs de l'utilisateur ont été mis à jour
        updated_user = User.objects.get(pseudo="johndoe")
        self.assertEqual(updated_user.name, "Updated")
        self.assertEqual(updated_user.firstname, "NewFirstName")

    def test_update_non_existing_user(self):
        # Tentez de mettre à jour un utilisateur qui n'existe pas
        updated = User.update_user(pseudo="nonexistentuser", name="Updated", firstname="NewFirstName")

        # Vérifiez que la mise à jour renvoie False
        self.assertFalse(updated)

    def test_read_existing_user(self):
        # Créez un utilisateur
        user = User.create_user(name="Doe", firstname="John", pseudo="johndoe")

        # Vérifiez que l'utilisateur a été créé
        self.assertIsNotNone(user)

        # Utilisez la méthode de classe pour récupérer l'utilisateur
        retrieved_user = User.read_user(pseudo="johndoe")

        # Vérifiez que l'utilisateur a été récupéré avec succès
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user, user)

    def test_read_non_existing_user(self):
        # Tentez de récupérer un utilisateur qui n'existe pas
        retrieved_user = User.read_user(pseudo="nonexistentuser")

        # Vérifiez que la méthode renvoie None
        self.assertIsNone(retrieved_user)
