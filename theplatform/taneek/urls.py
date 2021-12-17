from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('Connections',views.Connections,name="Connections"),
    path('About',views.About,name="About"),
    path('about_edit',views.about_edit,name="about_edit"),
    path('post',views.post,name="post"),
    path('search',views.search,name="search"),
]