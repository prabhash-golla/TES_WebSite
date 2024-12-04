from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Photo,File,Subscriber,contact # We import the photo model

# Register your models here.
admin.site.register(Photo)
admin.site.register(File)
admin.site.register(contact)
admin.site.register(Subscriber)