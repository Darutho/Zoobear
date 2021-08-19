from django.shortcuts import render

# Create your views here.
#views.py
from django.core.cache import cache
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from random import randint
from .models import Code
 
@csrf_protect

# def _get_pin(length=5):
#     """ Return a numeric PIN with length digits """
#     return randint(1000, 9999)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print "entered post"
        if form.is_valid():
            print "form valid"
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            subject = 'Verify Your Account'
            pin = randint(1000,9999)
            print pin
            # mob=pin
            cache.set('mob',pin, 24*3600)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            print username
            print password
            # kw= cache.get('mob')
            # print "cached code is: "
            # print kw
            # # q=Code(user=request.user,code=pin)
            # q.save()
            message = 'Hello! \n Thank You for registering with ZooBear. Your Verification Code is: '+ str(pin)+' \n Please enter this code in Profile Page to verify your account'
            from_email = settings.EMAIL_HOST_USER
            to_list =[form.cleaned_data['email']]
            send_mail(subject,message,from_email,to_list,fail_silently = True)
            print "send"
            user = authenticate(username=username,password=password)
            print "auth"
            if user is not None:
                login(request,user)
            else:
                print "i suck"
            print "ok"
            return render(request,'registration/success.html',None)
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render(request,'registration/success.html',None)
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'zoo/signed_in.html',
    { 'user': request.user }
    )
