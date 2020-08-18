from django import forms
from django.contrib.auth.models import User
from Blog_App.models import Blogger,Blog


class BloggerForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    about=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    profile_pic=forms.ImageField()


    class Meta():
        model=Blogger
        fields=('username','email','password','about','profile_pic')

class BlogForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    post=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    post_pic=forms.ImageField()
    #Blogger=forms.HiddenInput()

    class Meta():
        model=Blog
        fields=('title','post','post_pic')
