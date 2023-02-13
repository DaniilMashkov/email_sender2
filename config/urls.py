from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mailer.views import HomeListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeListView.as_view(), name='home'),
    path('', include('blog.urls', namespace='blog')),
    path('', include('mailer.urls', namespace='mailer')),
    path('', include('users.urls', namespace='users')),
    path('', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)