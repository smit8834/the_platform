from django.db import models
from django.conf import settings

class Posts(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    post_img = models.FileField(upload_to='media/', null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)