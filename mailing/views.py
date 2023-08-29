from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import ClientForm, MailingSettingForm, MessageForm
from mailing.models import Client, MailingSetting, Message, MailingLog
from mailing.services import send_mailing


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDetailView(DetailView):
    model = Client

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MailingSettingListView(ListView):
    model = MailingSetting


class MailingSettingCreateView(CreateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:mailingsetting_list')


class MailingSettingDetailView(DetailView):
    model = MailingSetting


class MailingSettingUpdateView(UpdateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:mailingsetting_list')


class MailingSettingDeleteView(DeleteView):
    model = MailingSetting
    success_url = reverse_lazy('mailing:mailingsetting_list')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    # def form_valid(self, form):
    #     new_mailing = form.save()
    #     now = timezone.now()
    #     new_mailing.created = now
    #     new_mailing.save()
    #
    #     send_mailing(new_mailing)
    #
    #     return super().form_valid(form)


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MailingLogDetail(DetailView):
    model = MailingLog
