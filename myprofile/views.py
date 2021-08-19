from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import ProfileForm,ProfileForm2
from django.contrib.auth.decorators import login_required
from .models import Year
from random import randint
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.cache import cache
from django.contrib import messages


@csrf_protect

@login_required
def newprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES or None,request.user)
        print "entered post"
        if form.is_valid():
            # print "form valid"
            # print "post variables", request.POST
            q=Year(user=request.user,first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],ph=form.cleaned_data['ph'])
            q.save()

            # user = User.objects.create_user(
            # username=form.cleaned_data['username'],
            # password=form.cleaned_data['password1'],
            # email=form.cleaned_data['email']
            # )
            print "redirecting"
            return HttpResponseRedirect('/login/home')
        return render(request, 'profile/errorprofile.html', {'form': ProfileForm})

    else:
        form = ProfileForm(request.user)
        # messages.add_message(request, messages.INFO, 'Hello world.')
        items = Year.objects.filter(user=request.user)
        if items:
            print items
            cdict={'profile':Year.objects.filter(user=request.user)}
            return render(request, 'profile/displayprofile.html',context=cdict)
        else:
            user = request.user
            return render(request,'profile/profile.html', {'form': ProfileForm, 'user':user})

@login_required
def updprofile(request):
    if request.method == 'POST':
        form = ProfileForm2(request.POST or None, request.FILES or None,request.user)
        print "entered upost"
        if form.is_valid():
            if Year.objects.filter(user=request.user).delete():
                q=Year(user=request.user,first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],ph=form.cleaned_data['ph'])
                q.save()
                print "redirecting"
            return HttpResponseRedirect('/login/home')
        return render(request, 'profile/errorprofile.html', {'form': ProfileForm})

    else:
        form = ProfileForm2(request.user)
        items = Year.objects.filter(user=request.user)
        if items:
            print items
            user = request.user
            return render(request,'profile/updprofile.html', {'form': ProfileForm2, 'user':user})
        else:
            return render(request,'profile/hack.html')
        
        # messages.add_message(request, messages.INFO, 'Hello world.')
        
        


@login_required
def otp(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES or None,request.user)
        print "entered post"
        if form.is_valid():
            # print "form valid"
            # print "post variables", request.POST
            q=Year(user=request.user,first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],ph=form.cleaned_data['ph'])
            q.save()

            # user = User.objects.create_user(
            # username=form.cleaned_data['username'],
            # password=form.cleaned_data['password1'],
            # email=form.cleaned_data['email']
            # )
            print "redirecting"
            return HttpResponseRedirect('/login/home')
        return render(request, 'profile/errorprofile.html', {'form': ProfileForm})
    else:
        pin = randint(1000,9999)
        print pin
        # mob=pin
        cache.set('mob',pin, 24*3600)
        subject="Verification Code"
        message = 'Hello! \n Your Verification Code is: '+ str(pin)+' \n Please enter this code in Profile Page to verify your account'
        from_email = settings.EMAIL_HOST_USER
        to_list =[request.user.email]
        send_mail(subject,message,from_email,to_list,fail_silently = True)
        user = request.user
        return render(request, 'profile/profile.html', {'form': ProfileForm, 'user':user})