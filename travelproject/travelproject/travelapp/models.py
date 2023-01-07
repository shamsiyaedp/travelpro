from distutils.command.upload import upload
from email.mime import image
import imghdr
from unicodedata import name
from django.db import models

# Create your models here.
class travel(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='img')
    desc=models.TextField()

    def __str__(self):
        return self.name