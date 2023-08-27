from django import forms

from mailing.models import Client, MailingSetting


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSettingForm(forms.ModelForm):
    class Meta:
        model = MailingSetting
        fields = '__all__'
