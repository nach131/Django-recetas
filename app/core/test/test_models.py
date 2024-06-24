"""
Test for models.
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


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
            ['Test2@42Barcelona.com', 'Test2@42barcelona.com'],
            ['TEST3@42BARCELONA.COM', 'TEST3@42barcelona.com'],
            ['test4@42barcelona.COM', 'test4@42barcelona.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'pass12345')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Tets that creating new user without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'pass12345')

    def test_create_superuser(self):
        """Test creating superuser"""
        user = get_user_model().objects.create_superuser(
            'supertest@42barcelona.com',
            'superpass12345',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            'test@42barcelona.com',
            "pass12345",
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='This is the Title',
            time_minutes=5,
            price=Decimal('5.50'),
            description='This is sample ricipe description',
        )

        self.assertEqual(str(recipe), recipe.title)
