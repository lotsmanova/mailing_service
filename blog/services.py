from django.conf import settings
from django.core.cache import cache

from blog.models import Blog


def get_blog_list_cache():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Blog.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Blog.objects.all()

    return category_list
