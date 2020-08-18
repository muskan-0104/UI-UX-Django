from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Blogger(models.Model):
    email=models.EmailField(primary_key=True)
    username=models.CharField(max_length=400)
    password = models.CharField(max_length=32)
    about=models.CharField(max_length=400)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.email


    def get_absolute_url(self):
        return reverse('home')

class Blog(models.Model):
    title=models.CharField(max_length=256)
    post=models.CharField(max_length=2000)
    date=models.DateTimeField()
    published_date=models.DateTimeField(blank=True,null=True)
    published=models.PositiveIntegerField()
    Blogger=models.ForeignKey(Blogger,related_name='eid',on_delete=models.PROTECT,default='SOME STRING')
    post_pic=models.ImageField(upload_to='post_pics',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


# Create your models here.

# Create your models here.
