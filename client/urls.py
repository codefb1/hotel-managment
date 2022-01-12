from django.conf.urls import url
from django.urls import path
from . import views
app_name='client'

urlpatterns=[
    path('', views.index),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('event.html', views.event, name='event'),
    path('restaurant.html', views.restaurant, name='restaurant'),
    path('lounge.html', views.lounge, name='lounge'),
    url(r'^bar$', views.bar, name='bar'),
    url(r'^booking$', views.booking, name='booking'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^menu$', views.menu, name='menu'),
    url(r'^registration/loginUser$', views.loginUser, name='loginUser'),
    url(r'^registration/registerUser$', views.registerUser, name='registerUser'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^searchresult$', views.searchresult, name='searchresult'),
    url(r'^registration/profileUser$', views.profileUser, name='profileUser'),
    url(r'^registration/edit_profileUser$', views.edit_profileUser, name='edit_profileUser')
]