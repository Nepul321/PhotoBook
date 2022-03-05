from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'caption')

        widgets = {
            'image' : forms.FileInput(attrs={'class' : 'form-control', 'accept' : 'image/*', 'required' : ''}),
            'caption' : forms.Textarea(attrs={'class' : 'form-control'})
        }
