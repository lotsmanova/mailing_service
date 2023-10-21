from django.test import TestCase
from django.test import Client
from users.models import User
from mailing.models import Client as Client_model


class BaseTestCase(TestCase):

    email = 'test@mail.ru'
    password = '12345'

    def setUp(self):
        # Создаем неавторизованный клиент
        self.client = Client()
        # Создаем пользователя
        self.user = User.objects.create(email=self.email)

        self.user.set_password(self.password)
        self.user.save()

        self.client.force_login(self.user)

        self.client_model = Client_model.objects.create(
            email='test2@mail.ru',
            first_name='Test2',
            last_name='Test2',
            user=self.user
        )

    def test_authorized(self):
        self.assertTrue(self.user.is_authenticated)
