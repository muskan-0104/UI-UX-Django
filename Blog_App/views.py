from Blog_App.forms import BloggerForm,BlogForm
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from . import models
from django import forms
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from Blog_App.models import Blog,Blogger
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.

#This view is for home page
class BlogListView(ListView):
    context_object_name='blog_list'
    model=models.Blog
    template_name='Home.html'

    def get(self,request):
        Blog_Data=Blog.objects.all()
        if request.session.has_key('email'):
            verify=True
            username = request.session['email']
            return render(request, 'Home.html', {'verify':verify,'blog_list' : Blog_Data})
        else:
            return render(request, 'Home.html', {'blog_list' : Blog_Data})

#this view is for blog detail page that is display when you click a blog on home page
class BlogDetailView(DetailView):
    context_object_name='blog_detail'
    model=models.Blog
    template_name='Post_Detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        if self.request.session.has_key('email'):
            context['verify']=True
            return context
        else:
            context['verify']=False
            return context


class AboutUsView(TemplateView):
    template_name='AboutUs.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        if self.request.session.has_key('email'):
            context['verify']=True
            return context
        else:
            context['verify']=False
            return context


class BloggerCreateView(CreateView):
    form_class = BloggerForm
    #fields=['username','email','password','about','profile_pic']
    model=models.Blogger
    template_name='SignUp.html'
    success_url ="/Home/"




def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        Blog_user=Blogger.objects.filter(email=email,password=password)
        if Blog_user:
            email=request.POST.get('email')
            request.session['email']=email
            Blog_Data=Blog.objects.filter(Blogger=email)
            my_dict={'verify':True,'email':Blog_Data}
            return render(request,'SignPost.html',context=my_dict)

        else:
            return HttpResponse("Invalid User")
    return render(request, 'SignIn.html', {})

def logout(request):
    my_dict={'verify':False}
    try:
        del request.session['email']
    except:
        pass
    return render(request,'Logout.html',context=my_dict)


class MyPostView(TemplateView):
    template_name='MyPost.html'
    def get(self,request):
        if request.session.has_key('email'):
            email = request.session['email']
            Blog_Data=Blog.objects.filter(Blogger=email)
            my_dict={'verify':True,'email':Blog_Data}
            return render(request, 'MyPost.html',context=my_dict)
        else:
            return render(request, 'MyPost.html', {'verify':False})


class DraftsView(TemplateView):
    template_name='Drafts.html'
    def get(self,request):
        if request.session.has_key('email'):
            verify=True
            email = request.session['email']
            Blog_Data=Blog.objects.filter(Blogger=email)
            my_dict={'verify':True,'email':Blog_Data}
            return render(request, 'Drafts.html',context=my_dict)
        else:
            return render(request, 'Drafts.html', {})

class MyPostDetailView(DetailView):
    context_object_name='mypost_detail'
    model=models.Blog
    template_name='MyPost_Detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['verify']=True
        return context

class MyPostCreateView(CreateView):
    form_class=BlogForm
    model=models.Blog
    template_name='NewPost.html'
    #success_url='/MyPost'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['verify']=True
        return context

    def form_valid(self, form):
        if self.request.session.has_key('email'):
            email=self.request.session.get('email')
        if self.request.POST.get('Publish'):
            obj = form.save(commit=False)
            obj.published = 1
            obj.published_date = timezone.now()
            obj.date=timezone.now()
            obj.Blogger=Blogger.objects.get(email=email)
            print(email)
            obj.save()
            return super(MyPostCreateView, self).form_valid(form)
        else:
            obj = form.save(commit=False)
            obj.published = 0
            obj.Blogger=Blogger.objects.get(email=email)
            obj.date=timezone.now()
            obj.save()
            return super(MyPostCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('Publish'):
            return reverse('mypost')
        else:
            return reverse('drafts')



class MyPostUpdateView(UpdateView):
    #fields=('title','post','post_pic')
    form_class=BlogForm
    model=models.Blog
    template_name='MyPostUpdate.html'
    success_url='/MyPost/'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['verify']=True
        return context




class MyPostDeleteView(DeleteView):
    context_object_name='mypost_detail'
    model=models.Blog
    success_url='/MyPost/'
    template_name='MyPost_Delete.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['verify']=True
        return context


class DraftsDetailView(DetailView):
    context_object_name='drafts_detail'
    model=models.Blog
    template_name='Drafts_Detail.html'
    success_url='/MyPost'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['verify']=True
        return context


class MyDraftUpdateView(UpdateView):
    fields=()
    context_object_name='mypost_detail'
    model=models.Blog
    template_name='Draft_Publish.html'
    success_url='/MyPost/'

    def form_valid(self, form):
        if self.request.POST.get('Publish'):
            obj = form.save(commit=False)
            obj.published = 1
            obj.published_date = timezone.now()
            obj.date=timezone.now()
            obj.save()
            return super(MyDraftUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['verify']=True
        return context
