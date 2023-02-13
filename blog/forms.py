from django import forms
from .models import Blog
from users.mixins import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'preview', 'status')

        widgets = {'content': forms.Textarea(attrs={'rows': 7, 'cols': 80}), }