from django import forms
from .models import Photo,File,Subscriber

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'tags']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file_title', 'file_author', 'file_description', 'file_thumbnail']
from django.db import models

from django import forms
from .models import Subscriber

class SubscriberForm(forms.Form):
    name = forms.CharField(max_length=100)
    roll_no = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=254)

from django import forms
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)



