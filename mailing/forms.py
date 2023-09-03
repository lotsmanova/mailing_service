from django import forms

from mailing.models import Client, MailingSetting, Message


class StyleFormMixin:
    """Общий стиль форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    """Форма для добавления клиента"""

    class Meta:
        model = Client
        exclude = ('user',)


class MailingSettingForm(StyleFormMixin, forms.ModelForm):
    """Форма для добавления настроек рассылки"""

    class Meta:
        model = MailingSetting
        exclude = ('user',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    """Форма для добавления сообщения рассылки"""

    class Meta:
        model = Message
        exclude = ('created',)
