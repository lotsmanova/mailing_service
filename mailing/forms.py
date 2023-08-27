from django import forms

from mailing.models import Client, MailingSetting, Message


class StyleFormMixin:
    """Общий стиль форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSettingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingSetting
        fields = '__all__'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
