from django.urls import path
from mailer.views import *
from mailer.apps import MailerConfig

app_name = MailerConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('reports/', ReportListView.as_view(), name='reports'),
    path('distributions/', DistributionListView.as_view(), name='distributions'),
    path('distribution_form/', DistributionCreateView.as_view(), name='create_distribution'),
    path('distribution_upd/<int:pk>/', DistributionUpdateView.as_view(), name='distribution_upd'),
    path('distribution_del/<int:pk>/', DistributionDeleteView.as_view(), name='distribution_del'),
    path('distributions_management/', DistributionManagerListView.as_view(), name='distributions_management'),
    path('switch_distrib/<int:pk>/', switch_distribution_status, name='switch_distribution_status'),
    path('switch_user/<int:pk>/', switch_user_status, name='switch_user_status'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('message_form/', MessageCreateView.as_view(), name='create_message'),
    path('message_upd/<int:pk>/', MessageUpdateView.as_view(), name='message_upd'),
    path('message_del/<int:pk>/', MessageDeleteView.as_view(), name='message_del'),
    path('recipients/', RecipientListView.as_view(), name='recipients'),
    path('recipient_form/', RecipientCreateView.as_view(), name='create_recipient'),
    path('recipient_upd/<int:pk>/', RecipientUpdateView.as_view(), name='recipient_upd'),
    path('recipient_del/<int:pk>/', RecipientDeleteView.as_view(), name='recipients_del'),
]