from django.urls import path, include
from blog.views import *
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog'),
    path('blog_form/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_upd/<int:pk>/', BlogUpdateView.as_view(), name='blog_upd'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]