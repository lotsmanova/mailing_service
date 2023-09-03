from django.core.management import BaseCommand

from mailing.cron import mailing_send


class Command(BaseCommand):
    """Кастомная команда для запуска рассылки"""
    def handle(self, *args, **options):

        mailing_send()
