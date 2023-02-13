from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView
from blog.services import get_blog_from_cache
from .forms import BlogForm
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = get_blog_from_cache()
        return context


class BlogDetailView(HitCountDetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    count_hit = True


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    permission_required = 'blog.add_blog'
    success_url = reverse_lazy('blog:blog')


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    permission_required = 'blog.add_blog'
    success_url = reverse_lazy('blog:blog')


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    permission_required = 'blog.add_blog'
    success_url = reverse_lazy('blog:blog')
