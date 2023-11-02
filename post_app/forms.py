from django import forms

from post_app.models import Post


class PostCreateForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('title', 'description', 'image')
