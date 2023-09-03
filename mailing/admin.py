from django.contrib import admin

from mailing.models import Client, MailingSetting, Message, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name',)


@admin.register(MailingSetting)
class MailingSettingAdmin(admin.ModelAdmin):
    list_filter = ('status', 'frequency', 'clients',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_subject', 'text_message',)

@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('last_attempt', 'status',)