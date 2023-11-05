from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from base.tests import BaseTestCase
from mailing.models import Client, MailingSetting, Message, MailingLog


class MailingTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.client_model = Client.objects.create(
            email='test2@mail.ru',
            first_name='Test2',
            last_name='Test2',
            user=self.user
        )

        self.mailing_setting = MailingSetting.objects.create(
            time_start='2023-08-08T00:00:00',
            time_end='2023-09-08T00:00:00',
            user=self.user
        )

        self.mailing_setting.clients.set([self.client_model])

        self.message = Message.objects.create(
            message_subject='Test subject',
            text_message='Test text',
            settings=self.mailing_setting
        )

        self.mailing_log = MailingLog.objects.create(
            last_attempt='2023-10-10T00:00:00',
            status='Test',
            mailing_set=self.message
        )

    def test_create_client(self):
        """Тестирование создания клиента"""

        data = {
            'email': 'test_create@mail.ru',
            'first_name': 'Test_create',
            'last_name': 'Test_create',
            'user': self.user
        }

        response = self.client.post(
            reverse('mailing:client_create'),
            data=data
        )

        new_client = Client.objects.get(email='test_create@mail.ru')

        self.assertEqual(new_client.first_name, 'Test_create')

    def test_list_client(self):
        """Тестирование вывода списка клиентов"""

        response = self.client.get(
            reverse('mailing:client_list')
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_detail_client(self):
        """Тестирование вывода клиента"""

        response = self.client.get(
            reverse('mailing:client_detail', kwargs={'pk': self.client_model.id})
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_delete_client(self):
        """Тестирование удаления клиента"""

        response = self.client.delete(
            reverse('mailing:client_delete', kwargs={'pk': self.client_model.id})
        )

        with self.assertRaises(Http404):
            get_object_or_404(Client, email='test2@mail.ru')

    def test_update_client(self):
        """Тестирование обновления клиента"""

        response = self.client.post(
            reverse('mailing:client_update', kwargs={'pk': self.client_model.id}),
            {'id': 2, 'email': 'test_update@mail.ru', 'first_name': 'test_update', 'last_name': 'test_update'}
        )

        update_client = Client.objects.get(email='test_update@mail.ru')

        self.assertEqual(update_client.first_name, 'test_update')

    def test_create_setting(self):
        """Тестирование создания настроек рассылки"""

        data = {
            'time_start': '2025-09-09T00:00:00',
            'time_end': '2026-10-08T00:00:00',
            'clients': [self.client_model],
            'user': self.user
        }

        response = self.client.post(
            reverse('mailing:mailingsetting_create'),
            data=data
        )

        self.assertEqual(response.status_code, 200)


    def test_list_setting(self):
        """Тестирование вывода списка настроек"""

        response = self.client.get(
            reverse('mailing:mailingsetting_list')
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_detail_setting(self):
        """Тестирование вывода настроек"""

        response = self.client.get(
            reverse('mailing:mailingsetting_detail', kwargs={'pk': self.mailing_setting.id})
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_delete_setting(self):
        """Тестирование удаления настроек"""

        response = self.client.delete(
            reverse('mailing:mailingsetting_delete', kwargs={'pk': self.mailing_setting.id})
        )

        with self.assertRaises(Http404):
            get_object_or_404(MailingSetting, time_start='2023-08-08T00:00:00')

    def test_update_setting(self):
        """Тестирование обновления настроек"""

        response = self.client.post(
            reverse('mailing:mailingsetting_update', kwargs={'pk': self.mailing_setting.id}),
            {'id': 1, 'time_start': '2024-08-08T00:00:00', 'time_end': '2024-09-08T00:00:00'}
        )
        self.assertEqual(response.status_code, 200)


    def test_create_message(self):
        """Тестирование создания сообщения"""

        data = {
            'message_subject': 'test_create',
            'text_message': 'test_create',
            'settings': self.mailing_setting
        }

        response = self.client.post(
            reverse('mailing:message_create'),
            data=data
        )

        self.assertEqual(response.status_code, 200)

    def test_list_message(self):
        """Тестирование вывода списка сообщений"""

        response = self.client.get(
            reverse('mailing:message_list')
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_detail_message(self):
        """Тестирование вывода сообщения"""

        response = self.client.get(
            reverse('mailing:message_detail', kwargs={'pk': self.message.id})
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_delete_message(self):
        """Тестирование удаления сообщения"""

        response = self.client.delete(
            reverse('mailing:message_delete', kwargs={'pk': self.message.id})
        )

        with self.assertRaises(Http404):
            get_object_or_404(Message, message_subject='subject')

    def test_update_message(self):
        """Тестирование обновления сообщения"""

        response = self.client.post(
            reverse('mailing:message_update', kwargs={'pk': self.message.id}),
            {'id': 1, 'message_subject': 'test_update', 'text_message': 'test_update'}
        )

        self.assertEqual(response.status_code, 200)

    def test_detail_log(self):
        """Тестирование вывода лог"""

        response = self.client.get(
            reverse('mailing:mailinglog_detail', kwargs={'pk': self.mailing_log.id})
        )

        self.assertEqual(
            response.status_code,
            200
        )
