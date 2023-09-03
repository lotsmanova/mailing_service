from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.templatetags.pytils_translit import slugify

from blog.forms import BlogForm
from blog.models import Blog
from blog.services import get_blog_list_cache


class BlogCreateView(CreateView):
    """Контроллер создания"""

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_net = form.save()
            new_net.slug = slugify(new_net.head)
            new_net.save()
        return super().form_valid(form)


class BlogListView(ListView):
    """Контроллер общего просмотра"""

    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_public=True)
        return queryset


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['subjects'] = get_blog_list_cache()
        return context_data


class BlogDetailView(DetailView):
    """Контроллер просмотра записи"""

    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """Контроллер редактирования"""
    model = Blog
    form_class = BlogForm


    def form_valid(self, form):
        if form.is_valid():
            new_net = form.save()
            new_net.slug = slugify(new_net.head)
            new_net.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    """Контроллер удаления"""
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


