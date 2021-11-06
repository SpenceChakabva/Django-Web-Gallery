from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# Using Class based views 

# Post tags model can be generated 
class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# Post details model
class Post(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True,blank=True, upload_to="images", default="placeholder.jpeg")
    body =  RichTextUploadingField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag,null=True)
    def __str__(self):
        return self.title
