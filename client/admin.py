# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Restaurant
admin.site.register(Restaurant)

from .models import Location
admin.site.register(Location)

from .models import Menu
admin.site.register(Menu)

from .models import Picture
admin.site.register(Picture)

from .models import User
admin.site.register(User)

from .models import Superuser
admin.site.register(Superuser)

from .models import Contact
admin.site.register(Contact)

from .models import boking
admin.site.register(boking)

from .models import Event
admin.site.register(Event)

from .models import msg
admin.site.register(msg)