from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from mailing.models import MailingSetting, MailingLog

def mailing_send():
    now = timezone.now()
    mailing_settings = MailingSetting.objects.filter(status__in=['created', 'started'])

    for mailing in mailing_settings:
        clients = mailing.clients.all()

        if mailing.time_start <= now <= mailing.time_end:
            if mailing.status == 'created':
                mailing.status = 'started'
                mailing.save()

            for client in clients:
                try:

                    mailing_message = mailing.message_set.first()

                    send_mail(
                        subject=mailing_message.message_subject,
                        message=mailing_message.text_message,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                        fail_silently=False,
                    )

                    mailing_log = MailingLog.objects.create(
                        last_attempt=timezone.now(),
                        status='Отправлено',
                        mailing_set=mailing_message,
                        successful_deliveries=1,
                    )
                    mailing_log.save()


                except Exception as e:
                    mailing_log = MailingLog.objects.create(
                        last_attempt=timezone.now(),
                        status='Ошибка отправки',
                        server_response=str(e),
                        mailing_set=mailing_message,
                    )
                    mailing_log.save()

        elif now > mailing.time_end:
            mailing.status = 'completed'
            mailing.save()