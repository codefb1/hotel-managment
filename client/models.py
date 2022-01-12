# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name                = models.CharField(max_length=100, blank=False)
    type                = models.CharField(max_length=100, blank=False)
    location            = models.CharField(max_length=150, blank=False)
    description         = models.CharField(max_length=1000, blank=True)
    manager_name        = models.CharField(max_length=100, blank=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    reservation_price   = models.CharField(max_length=50, blank=True)
    img_restaurant      = models.ImageField(upload_to='uploadRestaurant/')

    def __str__(self):
        return self.name + ' - ' + self.type + ' - ' + self.manager_name + ' - ' + self.location + ' - ' + self.description

class Location(models.Model):
    x= models.FloatField()
    y= models.FloatField()

    def __str__(self):
        return str(self.x) + ' - ' + str(self.y)

class Menu(models.Model):
    name            = models.CharField(max_length=100, blank=True)
    article         = models.CharField(max_length=100, blank=False)
    description     = models.CharField(max_length=1200, blank=True)
    type            = models.CharField(max_length=100, blank=False)
    price           = models.FloatField(blank=False)
    img_menu        = models.ImageField(upload_to='uploadMenu/')

    def __str__(self):
        return str(self.name) + ' - ' + str(self.article) + ' - ' + str(self.price) + ' - ' + str(self.type)

class Picture(models.Model):
    picture = models.URLField(max_length=1000)
    date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.picture) + ' - ' + str(self.date)

class User(models.Model):
    Username    = models.CharField(max_length=50, blank=False)
    email_user  = models.EmailField(max_length=50, blank=False)
    password    = models.CharField(max_length=50, blank=False)
    img_user    = models.ImageField(upload_to='uploadUser/')

    def __str__(self):
        return str(self.Username) + ' - ' + str(self.email_user) + ' - ' + str(self.password)

class Superuser(models.Model):
    Username = models.CharField(max_length=50, blank=False)
    email_user = models.EmailField(max_length=50, blank=False)
    psw_user   = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.Username) + ' - ' + str(self.email_user) + ' - ' + str(self.psw_user)

class Contact(models.Model):
    name    = models.CharField(max_length=100, blank=False)
    email   = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message    = models.CharField(max_length=1000, blank=False)
    date    = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name) + ' - ' + str(self.email) + ' - ' + str(self.subject) + ' - ' + str(self.date)

class boking(models.Model):
    name        = models.CharField(max_length=100, blank=False)
    firstname   = models.CharField(max_length=100, blank=False)
    lastname    = models.CharField(max_length=100, blank=False)
    email       = models.EmailField(max_length=100, blank=False)
    adress      = models.CharField(max_length=100, blank=False)
    phone       = models.CharField(max_length=100, blank=False)
    date        = models.DateField(auto_now_add=False)
    time        = models.TimeField(auto_now_add=False)
    
    def __str__(self):
        return str(self.firstname) + ' - ' + str(self.date) + ' - ' + str(self.time) + ' - ' + str(self.name)

class Event(models.Model):
    name           = models.CharField(max_length=100, blank=False)
    location       = models.CharField(max_length=150, blank=False)
    description    = models.CharField(max_length=1000, blank=True)
    responsible    = models.CharField(max_length=100, blank=True)
    contact        = models.CharField(max_length=100, blank=True)
    date           = models.DateField(auto_now_add=False)
    time           = models.TimeField(auto_now_add=False)
    img_event      = models.ImageField(upload_to='uploadEvent/')

    def __str__(self):
        return str(self.name) + ' - ' + str(self.date) + ' - ' + str(self.location)

class msg(models.Model):
    Username        = models.CharField(max_length=50, blank=False)
    Message         = models.CharField(max_length=5000, blank=False)
    date            = models.DateTimeField(auto_now_add=True)
    avis            = models.FloatField(blank=False)

    def __str__(self):
        return str(self.Username) + ' - ' + str(self.date) + ' - ' + str(self.avis)