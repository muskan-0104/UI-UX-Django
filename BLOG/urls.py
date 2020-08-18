"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Blog_App import views
from BLOG import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('Home/', views.BlogListView.as_view(),name='home'),
    path('About/', views.AboutUsView.as_view(),name='about'),
    path('SignUp/', views.BloggerCreateView.as_view(),name='signup'),
    path('Home/<int:pk>', views.BlogDetailView.as_view(),name='post_detail'),
    path('SignIn/',views.login,name='LogIn'),
    path('LogOut/',views.logout,name='LogOut'),
    path('MyPost/', views.MyPostView.as_view(),name='mypost'),
    path('Drafts/', views.DraftsView.as_view(),name='drafts'),
    path('Drafts/<int:pk>', views.DraftsDetailView.as_view(),name='drafts_detail'),
    path('MyPost/<int:pk>', views.MyPostDetailView.as_view(),name='mypost_detail'),
    path('Create/', views.MyPostCreateView.as_view(),name='mypost_create'),
    path('Update/<int:pk>', views.MyPostUpdateView.as_view(),name='mypost_update'),
    path('Delete/<int:pk>', views.MyPostDeleteView.as_view(),name='mypost_delete'),
    path('DraftUpdate/<int:pk>',views.MyDraftUpdateView.as_view(),name='mydraft_update')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
