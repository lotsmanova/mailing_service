from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import ClientForm, MailingSettingForm, MessageForm
from mailing.models import Client, MailingSetting, Message, MailingLog


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    login_url = reverse_lazy('users:login')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')
    login_url = reverse_lazy('users:login')


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    login_url = reverse_lazy('users:login')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')
    login_url = reverse_lazy('users:login')



class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')
    login_url = reverse_lazy('users:login')


class MailingSettingListView(LoginRequiredMixin, ListView):
    model = MailingSetting
    login_url = reverse_lazy('users:login')


class MailingSettingCreateView(LoginRequiredMixin, CreateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:mailingsetting_list')
    login_url = reverse_lazy('users:login')


class MailingSettingDetailView(LoginRequiredMixin, DetailView):
    model = MailingSetting
    login_url = reverse_lazy('users:login')


class MailingSettingUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:mailingsetting_list')
    login_url = reverse_lazy('users:login')


class MailingSettingDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSetting
    success_url = reverse_lazy('mailing:mailingsetting_list')
    login_url = reverse_lazy('users:login')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    login_url = reverse_lazy('users:login')
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_mailinglog = MailingLog.objects.latest('last_attempt')
        context['mailinglog'] = latest_mailinglog
        return context


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    login_url = reverse_lazy('users:login')


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    login_url = reverse_lazy('users:login')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    login_url = reverse_lazy('users:login')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')
    login_url = reverse_lazy('users:login')


class MailingLogDetail(LoginRequiredMixin, DetailView):
    model = MailingLog
    login_url = reverse_lazy('users:login')
