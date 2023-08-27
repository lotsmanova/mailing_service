# Generated by Django 4.2.4 on 2023-08-27 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt', models.DateTimeField(verbose_name='дата и время')),
                ('status', models.CharField(max_length=150, verbose_name='статус попытки')),
                ('server_response', models.CharField(blank=True, max_length=200, null=True, verbose_name='ответ сервера')),
                ('mailing_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'логи рассылки',
                'verbose_name_plural': 'логи рассылки',
            },
        ),
    ]