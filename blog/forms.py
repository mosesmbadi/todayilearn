from django import forms
from .models import *
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    body = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    content = RichTextField()

    class Meta:
        model  = Blog
        fields = ('title','body','content',)