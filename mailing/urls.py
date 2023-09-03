from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    MailingSettingListView, MailingSettingCreateView, MailingSettingDetailView, MailingSettingUpdateView, \
    MailingSettingDeleteView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, \
    MessageDeleteView, MailingLogDetail, HomeTemplateView

app_name = MailingConfig.name
urlpatterns = [
    path('', cache_page(60)(HomeTemplateView.as_view()), name='home_page'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('mailingsetting_list/', MailingSettingListView.as_view(), name='mailingsetting_list'),
    path('mailingsetting_create/', MailingSettingCreateView.as_view(), name='mailingsetting_create'),
    path('mailingsetting_detail/<int:pk>/', MailingSettingDetailView.as_view(), name='mailingsetting_detail'),
    path('mailingsetting_update/<int:pk>/', MailingSettingUpdateView.as_view(), name='mailingsetting_update'),
    path('mailingsetting_delete/<int:pk>/', MailingSettingDeleteView.as_view(), name='mailingsetting_delete'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('mailinglog_detail/<int:pk>/', MailingLogDetail.as_view(), name='mailinglog_detail'),
]
