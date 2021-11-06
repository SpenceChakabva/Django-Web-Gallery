from django import forms
from django.forms import ModelForm
# Import post from models
from .models import Post

# PostForm for interacting with post data
class PostForm(ModelForm):
    # Use prebuild django modelform
    class Meta:
        model = Post
        fields = '__all__'
        # Assign checkbox widget out tags
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }