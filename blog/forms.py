from blog.models import Blog
from mailing.forms import StyleFormMixin
from django import forms

class BlogForm(StyleFormMixin, forms.ModelForm):
    """Форма создания блога"""

    class Meta:
        model = Blog
        fields = ('head', 'body', 'preview', 'date_create',)
