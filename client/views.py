# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant,Location,Menu,Picture,User,Superuser,Contact,boking,Event,msg
from django.views import View
from django.views.generic import ListView
from .forms import userForm, bookingForm, loginForm, profileForm, msgForm, contactForm, searchForm
from django.contrib.auth import logout
from django.db.models import Min
# Create your views here.

def index(request):
    r = Restaurant.objects.order_by('-updated')[:6]
    rr = Restaurant.objects.count()
    e = Event.objects.order_by('-date')
    m = msg.objects.order_by('-date')
    x = e.count()

    r = Restaurant.objects.filter(
        Q(type__iexact='restaurant') |
        Q(type__icontains='resto'))
    re = r.count()

    l = Restaurant.objects.filter(
        Q(type__iexact='lounge') |
        Q(type__icontains='lounge'))
    le = l.count()

    b = Restaurant.objects.filter(
        Q(type__iexact='bar') |
        Q(type__icontains='bar'))
    ba = b.count()
    
    res = boking.objects.count()

    us = User.objects.count()

    formsearch = searchForm(request.POST)
    #for form search
    """
    return render_to_response("books/create.html", {
        "form": form,
    }, context_instance=RequestContext(request))
    """

    return render(request, 'index.html', {'r':r, 'e':e, 'm':m, 'x':x, 'rr':rr, 're':re, 'le':le, 'ba':ba, 'res':res, 'us':us, 'formsearch':formsearch})

def event(request):
    y = request.GET.get('id')
    y = Event.objects.get(name=y)
    return render(request, 'event.html', {'y':y})

def about(request):
    m = msg.objects.all()
    return render(request, 'about.html', {'m':m})

def restaurant(request):
    r = Restaurant.objects.filter(
        Q(type__iexact='restaurant') |
        Q(type__icontains='resto'))
    y = r.order_by('-updated')
    x = r.count()
    return render(request, 'restaurant.html', {'y': y, 'x':x})

def lounge(request):
    y = Restaurant.objects.filter(
        Q(type__iexact='lounge') |
        Q(type__icontains='lounge'))
    l = y.order_by('-updated')
    x = l.count()
    return render(request, 'lounge.html', {'l':l, 'x':x})

def bar(request):
    y = Restaurant.objects.filter(
        Q(type__iexact='bar') |
        Q(type__icontains='bar'))
    b = y.order_by('-updated')
    x = b.count()
    return render(request, 'bar.html', {'b':b, 'x':x})

def booking(request):
    y = request.GET.get('id')
    y = Restaurant.objects.get(name=y)
    formbooking = bookingForm(request.POST)
    b = boking()
    if formbooking.is_valid():
        b.name      = y.name
        b.firstname = formbooking.cleaned_data['firstname']
        b.lastname  = formbooking.cleaned_data['lastname']
        b.email     = formbooking.cleaned_data['email']
        b.adress    = formbooking.cleaned_data['adress']
        b.phone     = formbooking.cleaned_data['phone']
        b.date      = formbooking.cleaned_data['date']
        b.time      = formbooking.cleaned_data['time']
        b.save()
        return redirect('client:index')
    else:
        formbooking = bookingForm
    return render(request, 'booking.html', {'formbooking' : formbooking, 'y':y})

def contact(request):  
    c = Contact()
    formcontact = contactForm(request.POST)
    if request.method == 'POST' and formcontact.is_valid():
        c.name          = formcontact.cleaned_data['name']
        c.email         = formcontact.cleaned_data['email']
        c.subject       = formcontact.cleaned_data['subject']
        c.message       = formcontact.cleaned_data['message']
        c.save()
        return redirect('client:contact')
    else:
        formcontact = contactForm()
    return render(request, 'contact.html', {'formcontact' : formcontact})

def menu(request):
    y = request.GET.get('id')
    y = Restaurant.objects.get(name=y)
    x = Menu.objects.filter(
        Q(name__iexact= y.name) |
        Q(name__icontains= y.name))
    
    a = Menu.objects.filter(
        Q(name__iexact= y.name),
        Q(type= 'main'))
    aa = a.count()

    de = Menu.objects.filter(
        Q(name__iexact= y.name),
        Q(type__iexact='dessert'))
    dede = de.count()

    dr = Menu.objects.filter(
        Q(name__iexact= y.name),
        Q(type__iexact='drinks'))
    drdr = dr.count()

    form = msgForm(request.POST)
    m = msg()
    if form.is_valid():
        m.Username          = form.cleaned_data['Username']
        m.Message           = form.cleaned_data['Message']
        m.avis              = form.cleaned_data['avis']
        m.save()
        return redirect('client:index')
    else:
        form = msgForm()
    
    return render(request, 'menu.html', {'y' : y , 'x':x, 'a':a, 'aa':aa, 'de':de, 'dede':dede, 'dr':dr, 'drdr':drdr, 'form' : form})

def registerUser(request):
    form = userForm(request.POST)
    m = User()
    if form.is_valid():
        m.Username          = form.cleaned_data['Username']
        m.email_user        = form.cleaned_data['email_user']
        m.password          = form.cleaned_data['password']
        m.repeat_password   = form.cleaned_data['repeat_password']
        m.img_user          = form.cleaned_data['img_user']
        m.save()
        return redirect('client:loginUser')
    else:
        form = userForm()
    return render(request, 'registration/registerUser.html', {'form' : form})

def loginUser(request):
    formlogin = loginForm(request.POST)
    y = False
    if formlogin.is_valid():
        email_user        = formlogin.cleaned_data['email_user']
        password          = formlogin.cleaned_data['password']
        try:
            y = User.objects.get(email_user=email_user, password=password)
        except User.DoesNotExist as e:
            pass
        if y:
            request.session['member_Username'] = y.Username
            return redirect('client:index')
        else:
            return redirect('client:loginUser')
    else:
        formlogin = loginForm()
    return render(request, 'registration/loginUser.html', {'formlogin' : formlogin})

def logout_view(request):
    request.session.delete()
    return render(request, 'index.html')

def profileUser(request):
    y = request.GET.get('id')
    y = User.objects.get(Username=y)
    u = userForm()
    return render(request, 'registration/profileUser.html', {'u' : u , 'y':y })

def edit_profileUser(request):
    y = request.GET.get('id')
    y = User.objects.get(Username=y)
    print("y is ")
    print(y)
    print(y.Username)
    form1 = profileForm(request.POST or None, request.FILES or None)
    print(form1.is_valid())
    if request.method == 'POST':
        Username        = form1.cleaned_data['Username']
        """img_user          = form1.cleaned_data['img_user']"""
        email_user        = form1.cleaned_data['email_user']
        password          = form1.cleaned_data['password']
        
        y.Username = Username
        y.email_user = email_user
        y.password = password
        """y.img_user = img_user"""
        y.save()
        request.session['y.Username'] = y.Username
        #error: update picture
        #error: update session
        """
        request.session.modified = True"""
        
        return redirect('client:index')
        
    
    return render(request, 'registration/edit_profileUser.html', {'y':y , 'form1':form1})

def searchresult(request):
    formsearch = searchForm(request.POST)
    if formsearch.is_valid():
        name        = formsearch.cleaned_data['name']
        print('name is')
        print(name)
        location    = formsearch.cleaned_data['location']
        y = Restaurant.objects.filter(
            Q(location__icontains= location),
            Q(name__icontains= name))
        a=y.count()
        print(y)
    return render(request, 'searchresult.html', {'a':a,'y':y , 'formsearch':formsearch})
        