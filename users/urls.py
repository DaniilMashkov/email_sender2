from django.urls import path, re_path
from .apps import UsersConfig
from .views import *


app_name = UsersConfig.name

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signed/', SignedView.as_view(), name='signed'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('activated/', ActivatedView.as_view(), name='activated'),
]
