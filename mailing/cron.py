from django.core.mail import send_mail
from django.utils import timezone

from mailing.models import MailingSetting, MailingLog

def mailing_send():
    now = timezone.now()
    settings = MailingSetting.objects.filter(status__in=['created', 'started'])

    for mailing in settings:
        clients = mailing.clients.all()

        if mailing.time_start <= now <= mailing.time_end:
            if mailing.status == 'created':
                mailing.status = 'started'
                mailing.save()

            for client in clients:
                try:
                    send_mail(
                        mailing.message_subject,
                        mailing.text_message,
                        settings.EMAIL_HOST_USER,
                        [client.email],
                        False,
                    )

                    mailing_log = MailingLog.objects.create(
                        last_attempt=timezone.now(),
                        status='Отправлено',
                        mailing_set=mailing,
                    )
                    mailing_log.save()


                except Exception as e:
                    mailing_log = MailingLog.objects.create(
                        last_attempt=timezone.now(),
                        status='Ошибка отправки',
                        server_response=str(e),
                        mailing_set=mailing,
                    )
                    mailing_log.save()

        elif now > mailing.time_end:
            mailing.status = 'completed'
            mailing.save()
