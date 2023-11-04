from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
    def test_create_user(self):
        # Create a user with a username that does not exist yet
        user = User.create_user(name="Doe", firstname="John", username="johndoe")

        # Verify that the user has been created
        self.assertIsNotNone(user)

        # Verify that the user can be retrieved from the database
        saved_user = User.objects.get(username="johndoe")
        self.assertEqual(saved_user, user)

    def test_create_user_with_existing_username(self):
        # Create a user with a username that already exists
        existing_user = User.create_user(name="Smith", firstname="Jane", username="janesmith")
        self.assertIsNotNone(existing_user)

        user = User.create_user(name="Doe", firstname="John", username="janesmith")

        # Verify that the user has not been created (should return None)
        self.assertIsNone(user)

    def test_create_user_with_same_username(self):
        # Create two users with the same username
        user1 = User.create_user(name="Doe", firstname="John", username="johndoe")
        user2 = User.create_user(name="Smith", firstname="Jane", username="johndoe")

        # Verify that the first user is created
        self.assertIsNotNone(user1)

        # Verify that the second user is not created (should raise an error message)
        self.assertIsNone(user2, "A user with the same username already exists.")

    def test_delete_user(self):
        # Create a user
        user = User.create_user(name="Van Bellinghen", firstname="Brandon", username="Zenthor")

        # Verify that the user has been created
        self.assertIsNotNone(user)

        # Delete the user using the instance method
        deleted = user.delete_user(username="Zenthor")

        # Verify that the user has been deleted
        self.assertTrue(deleted)

        # Verify that the user no longer exists in the database
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username="Zenthor")

    def test_delete_non_existing_user(self):
        # Try to delete a user that does not exist
        deleted = User.delete_user(username="nonexistentuser")

        # Verify that the deletion returns False
        self.assertFalse(deleted)

    def test_update_existing_user(self):
        # Create a user
        user = User.create_user(name="Doe", firstname="John", username="johndoe")

        # Verify that the user has been created
        self.assertIsNotNone(user)

        # Update the user using the class method
        updated = User.update_user(username="johndoe", name="Updated", firstname="NewFirstName")

        # Verify that the user has been updated successfully
        self.assertTrue(updated)

        # Verify that the user's attributes have been updated
        updated_user = User.objects.get(username="johndoe")
        self.assertEqual(updated_user.name, "Updated")
        self.assertEqual(updated_user.firstname, "NewFirstName")

    def test_update_non_existing_user(self):
        # Try to update a user that does not exist
        updated = User.update_user(username="nonexistentuser", name="Updated", firstname="NewFirstName")

        # Verify that the update returns False
        self.assertFalse(updated)

    def test_read_existing_user(self):
        # Create a user
        user = User.create_user(name="Doe", firstname="John", username="johndoe")

        # Verify that the user has been created
        self.assertIsNotNone(user)

        # Use the class method to retrieve the user
        retrieved_user = User.read_user(username="johndoe")

        # Verify that the user has been successfully retrieved
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user, user)

    def test_read_non_existing_user(self):
        # Try to retrieve a user that does not exist
        retrieved_user = User.read_user(username="nonexistentuser")

        # Verify that the method returns None
        self.assertIsNone(retrieved_user)
