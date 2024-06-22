"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = 'test@enunpimpam.com'
        password = '12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests email is normalized for new users."""
        sample_emails = [
            ['test1@42BARCELONA.com', 'test1@42barcelona.com'],
            ['Test2@42Barcelona.com' ,'Test2@42barcelona.com'],
            ['TEST3@42BARCELONA.COM', 'TEST3@42barcelona.com'],
            ['test4@42barcelona.COM', 'test4@42barcelona.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'pass12345')
            self.assertEqual(user.email, expected)
