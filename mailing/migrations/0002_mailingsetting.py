# Generated by Django 4.2.4 on 2023-08-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(verbose_name='дата и время начала рассылки')),
                ('time_end', models.DateTimeField(verbose_name='дата и время окончания рассылки')),
                ('frequency', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], default='Раз в месяц', max_length=50, verbose_name='период рассылки')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('completed', 'Завершена')], default='Создана', max_length=20, verbose_name='статус рассылки')),
                ('clients', models.ManyToManyField(to='mailing.client', verbose_name='клиенты')),
            ],
            options={
                'verbose_name': 'настройки рассылки',
                'verbose_name_plural': 'настройки рассылки',
            },
        ),
    ]
