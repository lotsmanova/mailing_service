from django import forms

from mailing.models import Client, MailingSetting, Message


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSettingForm(forms.ModelForm):
    class Meta:
        model = MailingSetting
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
