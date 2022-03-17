from profiles.models import Profile
from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'is_private', 'caption')

        widgets = {
            'image' : forms.FileInput(attrs={'class' : 'form-control', 'accept' : 'image/*', 'required' : ''}),
            'caption' : forms.Textarea(attrs={'class' : 'form-control'})
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'location')

        widgets = {
            'bio' : forms.Textarea(attrs={'class' : 'form-control'}),
            'location' : forms.TextInput(attrs={'class' : 'form-control'})
        }