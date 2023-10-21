from django.urls import reverse
from base.tests import BaseTestCase
from mailing.models import Client

class MailingTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.client_model = Client.objects.create(
            email='test2@mail.ru',
            first_name='Test2',
            last_name='Test2',
            user=self.user
        )

    # def log_in_user(self):
    #     response = self.client.post(
    #         reverse('users:login'),
    #         data={'email': self.email, 'password': self.password},
    #         follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(self.user.is_authenticated)
    #
    # def test_create_client(self):
    #     """Тестирование создания клиента"""
    #
    #     self.log_in_user()
    #
    #     data = {
    #         'email': 'test3@mail.ru',
    #         'first_name': 'Test',
    #         'last_name': 'Test'
    #     }
    #
    #     response = self.client.post(
    #         reverse('mailing:client_create'),
    #         data=data
    #     )
    #
    #     print(response.status_code)
    #     print(response.content)
    #     # print(response.redirect_chain)
    #
    #     self.assertEqual(
    #         response.status_code,
    #         201
    #     )

    def test_create_client(self):
        """Тестирование создания клиента"""

        data = {
            'email': 'test3@mail.ru',
            'first_name': 'Test',
            'last_name': 'Test'
        }

        response = self.client.post(
            reverse('mailing:client_create'),
            data=data
        )
        print(response.status_code)
        print(response.content)

        self.assertEqual(
            response.status_code,
            201
        )

    def test_list_client(self):
        """Тестирование вывода списка клиентов"""

        response = self.client.get(
            reverse('mailing:client_list')
        )

        self.assertEqual(
            response.status_code,
            200
        )
