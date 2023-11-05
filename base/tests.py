from django.test import TestCase, Client
from users.models import User



class BaseTestCase(TestCase):

    email = 'test@mail.ru'
    password = '12345'

    def setUp(self):
        # Создаем неавторизованный клиент
        self.client = Client()
        # Создаем пользователя
        self.user = User.objects.create(email=self.email, is_active=True)

        self.user.set_password(self.password)
        self.user.save()

        self.client.force_login(self.user)

    def test_authorized(self):
        self.assertTrue(self.user.is_authenticated)
