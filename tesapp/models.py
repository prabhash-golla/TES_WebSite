from django.db import models
import uuid,os

# Create your models here.
from django.db import models

from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager

from django.utils import timezone

def generate_upload_path(instance, filename):
     # Generate a unique filename for the uploaded file
     filename = f'{uuid.uuid4()}{os.path.splitext(filename)[1]}'
     # Return the upload path
     return f'photos/{filename}'

class Photo(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')
    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class File(models.Model):
    file_title = models.CharField(max_length=45)
    file_author = models.CharField(max_length=45)
    file_description = models.CharField(max_length=250)
    file_thumbnail = models.ImageField(upload_to='file_image/', default='default_thumbnail.jpg')
    file_created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files/')
    file_submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    sas_url = models.URLField(blank=True)

    def __str__(self):
        return self.file_title
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class contact(models.Model):
    name = models.CharField( max_length=50)
    message = models.CharField( max_length=500)

    def __str__(self):
        return self.name