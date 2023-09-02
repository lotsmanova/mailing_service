from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import ClientForm, MailingSettingForm, MessageForm
from mailing.models import Client, MailingSetting, Message, MailingLog


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер списка клиентов"""

    model = Client
    login_url = reverse_lazy('users:login')


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания клиентов"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')
    login_url = reverse_lazy('users:login')


class ClientDetailView(LoginRequiredMixin, DetailView):
    """Контроллер просмотра клиента"""

    model = Client
    login_url = reverse_lazy('users:login')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменения клиента"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')
    login_url = reverse_lazy('users:login')



class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления клиента"""

    model = Client
    success_url = reverse_lazy('mailing:client_list')
    login_url = reverse_lazy('users:login')


class MailingSettingListView(LoginRequiredMixin, ListView):
    """Контроллер списка настроек рассылки"""

    model = MailingSetting
    login_url = reverse_lazy('users:login')


class MailingSettingCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания настроек рассылки"""

    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:mailingsetting_list')
    login_url = reverse_lazy('users:login')


class MailingSettingDetailView(LoginRequiredMixin, DetailView):
    """Контроллер просмотра настроек рассылки"""

    model = MailingSetting
    login_url = reverse_lazy('users:login')


class MailingSettingUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменения настроек рассылки"""

    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:mailingsetting_list')
    login_url = reverse_lazy('users:login')


class MailingSettingDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления настроек рассылки"""

    model = MailingSetting
    success_url = reverse_lazy('mailing:mailingsetting_list')
    login_url = reverse_lazy('users:login')


class MessageListView(LoginRequiredMixin, ListView):
    """Контроллер списка сообщений рассылки"""

    model = Message
    login_url = reverse_lazy('users:login')
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            latest_mailinglog = MailingLog.objects.latest('last_attempt')
            context['mailinglog'] = latest_mailinglog
        except MailingLog.DoesNotExist:
            context['mailinglog'] = None
        return context


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания сообщений рассылки"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    login_url = reverse_lazy('users:login')


class MessageDetailView(LoginRequiredMixin, DetailView):
    """Контроллер просмотра сообщений рассылки"""

    model = Message
    login_url = reverse_lazy('users:login')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменения сообщений рассылки"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    login_url = reverse_lazy('users:login')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления сообщений рассылки"""

    model = Message
    success_url = reverse_lazy('mailing:message_list')
    login_url = reverse_lazy('users:login')


class MailingLogDetail(LoginRequiredMixin, DetailView):
    """Контроллер просмотра логов рассылки"""

    model = MailingLog
    login_url = reverse_lazy('users:login')
