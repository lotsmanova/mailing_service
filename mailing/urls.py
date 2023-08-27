from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    MailingSettingListView, MailingSettingCreateView, MailingSettingDetailView, MailingSettingUpdateView, \
    MailingSettingDeleteView

app_name = MailingConfig.name
urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('mailingsetting_list/', MailingSettingListView.as_view(), name='mailingsetting_list'),
    path('mailingsetting_create/', MailingSettingCreateView.as_view(), name='mailingsetting_create'),
    path('mailingsetting_detail/<int:pk>/', MailingSettingDetailView.as_view(), name='mailingsetting_detail'),
    path('mailingsetting_update/<int:pk>/', MailingSettingUpdateView.as_view(), name='mailingsetting_update'),
    path('mailingsetting_delete/<int:pk>/', MailingSettingDeleteView.as_view(), name='mailingsetting_delete'),
]