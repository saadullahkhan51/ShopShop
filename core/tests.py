from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='jon',
            email='jon@email.com',
            password='jonjon1'
        )
        self.assertEqual(user.username, 'jon')
        self.assertEqual(user.email, 'jon@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    

