from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}

class Client(models.Model):
    """Модель клиента"""

    email = models.EmailField(max_length=150, verbose_name='почта')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    comments = models.TextField(verbose_name='комментарий', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)


    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'


    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class MailingSetting(models.Model):
    """Модель настройки"""

    FREQUENCY_CHOICES = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )

    STATUS_CHOICES = (
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    )

    time_start = models.DateTimeField(verbose_name='дата и время начала рассылки')
    time_end = models.DateTimeField(verbose_name='дата и время окончания рассылки')
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, verbose_name='период рассылки', default='Раз в месяц')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='статус рассылки', default='Создана')
    clients = models.ManyToManyField(Client, verbose_name='клиенты')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь',
                             **NULLABLE)



    def __str__(self):
        return f'{self.time_start} ({self.status})'


    class Meta:
        verbose_name = 'настройки рассылки'
        verbose_name_plural = 'настройки рассылки'


class Message(models.Model):
    """Модель сообщения"""

    created = models.DateTimeField(verbose_name='отправка', **NULLABLE)
    message_subject = models.CharField(max_length=200, verbose_name='тема сообщения')
    text_message = models.TextField(verbose_name='тело сообщения')
    settings = models.ForeignKey(MailingSetting, on_delete=models.CASCADE, verbose_name='настройки')


    def __str__(self):
        return f'{self.message_subject}'


    class Meta:
        verbose_name = 'сообщение рассылки'
        verbose_name_plural = 'сообщения рассылки'


class MailingLog(models.Model):
    """Модель логов"""

    last_attempt = models.DateTimeField(verbose_name='дата и время')
    status = models.CharField(max_length=150, verbose_name='статус попытки')
    server_response = models.CharField(max_length=200, verbose_name='ответ сервера', **NULLABLE)
    mailing_set = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')
    successful_deliveries = models.IntegerField(default=0, verbose_name='успешно доставлено')


    def __str__(self):
        return f'{self.last_attempt} ({self.status})'


    class Meta:
        verbose_name = 'логи рассылки'
        verbose_name_plural = 'логи рассылки'
