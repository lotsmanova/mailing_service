from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import ClientForm, MailingSettingForm
from mailing.models import Client, MailingSetting, Message


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

