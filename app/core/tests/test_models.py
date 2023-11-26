from django.test import TestCase
from django.contrib.auth import get_user_model

from decimal import Decimal
from core import models

class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        email = "test@example.com"
        password = "testpassword" 
        
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_emailnormalized(self):
        pass
    
    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123"
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        