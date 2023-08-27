from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils import timezone

from mailing.models import MailingSetting, Message, MailingLog


def send_mailing(mailing):
    setting = MailingSetting.objects.get(id=mailing.settings.pk)

    clients = setting.clients.all()

    now = timezone.now()

    if setting.time_end > now > setting.time_start:
        for client in clients:
            try:
                send_mail(
                    mailing.message_subject,
                    mailing.text_message,
                    settings.EMAIL_HOST_USER,
                    [client.email],
                    False,
                )

                MailingLog.objects.create(
                    last_attempt=datetime.now(),
                    status='Отправлено',
                    mailing_set=mailing,
                )
            except Exception as e:
                MailingLog.objects.create(
                    last_attempt=datetime.now(),
                    status='Ошибка отправки',
                    server_responce=str(e),
                    mailing_set=mailing,
                )
        setting.status = 'Завершена'
        setting.save()


