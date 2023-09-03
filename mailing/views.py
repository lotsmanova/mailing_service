from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blog.models import Blog
from mailing.forms import ClientForm, MailingSettingForm, MessageForm
from mailing.models import Client, MailingSetting, Message, MailingLog

class HomeTemplateView(TemplateView):
    """Контроллер домашней страницы"""

    template_name = 'mailing/home_list.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        # Количество рассылок всего
        total_mailings = MailingSetting.objects.count()
        context_data['total_mailings'] = total_mailings

        # Количество активных рассылок
        total_active_mailing = MailingSetting.objects.filter(status__in=['created', 'started']).count()
        context_data['total_active_mailing'] = total_active_mailing

        # Количество уникальных клиентов
        total_unique_client = Client.objects.filter(mailingsetting__isnull=False).distinct().count()
        context_data['total_unique_client'] = total_unique_client

        # 3 случайные записи из блога
        blog = Blog.objects.all()
        if blog:
            blog_write = sample(list(blog), 3)
            context_data['blog_write'] = blog_write
        else:
            context_data['blog_write'] = None

        return context_data


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер списка клиентов"""

    model = Client
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания клиентов"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


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

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class MailingSettingCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания настроек рассылки"""

    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:mailingsetting_list')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


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

    def get_queryset(self):
        return super().get_queryset().filter(settings__user=self.request.user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания сообщений рассылки"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.settings = MailingSetting.objects.get(user=self.request.user)
        self.object.save()

        return super().form_valid(form)


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
