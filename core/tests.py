from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Product


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

class IndexPageTests(TestCase):
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)
        self.user = get_user_model().objects.create_user(
            username = 'test',
            email = 'test@mail.com',
            password = 'testpass'
        )
        self.post = Product.objects.create(
            title = 'test product',
            price = 200,
            count = 4,
            collection = 'Summer',
            description = 'Test product description',
            slug = 'test-prod'
        )

    def test_string_representation(self):
        prod = Product(title='test product', price=200)
        self.assertEqual(str(prod), f"{prod.title}, {prod.price}")

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_template(self):
        self.assertTemplateUsed(self.response, 'core/index.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'SHOP')
        self.assertContains(self.response, 'View Cart')
    

    

    

