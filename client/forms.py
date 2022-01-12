from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class userForm(forms.Form):
    Username        = forms.CharField(max_length=100)
    img_user        = forms.ImageField()
    email_user      = forms.EmailField(max_length=100)
    password        = forms.CharField(max_length=50, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=50)

class bookingForm(forms.Form):
    firstname       = forms.CharField(max_length=100)
    lastname        = forms.CharField(max_length=100)
    email           = forms.EmailField(max_length=100)
    adress          = forms.CharField(max_length=100)
    phone           = forms.CharField(max_length=100)
    date            = forms.DateField()
    time            = forms.TimeField()

class loginForm(forms.Form):
    email_user      = forms.EmailField(max_length=100)
    password        = forms.CharField(max_length=50, widget=forms.PasswordInput)

class profileForm(forms.Form):
    Username        = forms.CharField(max_length=100)
    img_user        = forms.ImageField()
    email_user      = forms.EmailField(max_length=100)
    password        = forms.CharField(max_length=50, widget=forms.PasswordInput)

class msgForm(forms.Form):
    Username        = forms.CharField(max_length=50)
    Message         = forms.CharField(max_length=5000)
    avis            = forms.FloatField(
        validators=[MinValueValidator(0.9), MaxValueValidator(10)],
    )

class contactForm(forms.Form):
    name            = forms.CharField(max_length=50)
    email           = forms.CharField(max_length=100)
    subject         = forms.CharField(max_length=100)
    message         = forms.CharField(max_length=5000)

class searchForm(forms.Form):
    name            = forms.CharField(max_length=100,required = False)
    location        = forms.CharField(max_length=150,required = False)