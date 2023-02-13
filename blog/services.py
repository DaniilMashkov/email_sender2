from blog.models import Blog
from django.conf import settings
from django.core.cache import cache


def get_blog_from_cache():
    if settings.CACHE_ENABLED:
        return cache.get_or_set('blog', Blog.objects.all())
    return Blog.objects.all()