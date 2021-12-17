from django.db.models import fields
from django.forms import ModelForm
from .models import *

class PostForm (ModelForm):
    class Meta:
        model=Posts
        fields = ['title','post_img']