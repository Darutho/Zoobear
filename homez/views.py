from django.shortcuts import render
from .forms import ComplaintForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def home(request):
    # context_dict={'boldmessage': Courier.objects.all() }
    nothing = {}
    if request.user.is_authenticated() == True and request.user.is_active == True:
      return render(request,'zoo/signed_in.html',context=nothing)
    else:
      return render(request,'zoo/index.html',context=nothing)
def tutorial(request):
    # context_dict={'boldmessage': Courier.objects.all() }
    nothing = {}
    return render(request,'zoo/tutorial.html',context=nothing)
def contact(request):
    if request.method == 'POST':
      form = ComplaintForm(request.POST)
      print "not yet valid"
      print "post variables", request.POST
      if form.is_valid():
         print "valid"
         from_email=settings.EMAIL_HOST_USER
         subject = form.cleaned_data['feedback']
         message = "Hello, I am " + str(form.cleaned_data['name']) + "\n "+ str(form.cleaned_data['details'])
         from_email = settings.EMAIL_HOST_USER
         me="contact.anant1@gmail.com"
         to_list =[me]
         send_mail(subject,message,from_email,to_list,fail_silently = True)
         return HttpResponseRedirect('/')
      print "invaluid"
      return render(request, 'zoo/contact.html', {'form': ComplaintForm})
    else:
      form = ComplaintForm()
      return render(request,'zoo/contact.html', {'form': ComplaintForm})

def faq(request):
    # context_dict={'boldmessage': Courier.objects.all() }
    nothing = {}
    return render(request,'zoo/faq.html',context=nothing)
def bookguide(request):
    # context_dict={'boldmessage': Courier.objects.all() }
    nothing = {}
    return render(request,'zoo/bookguide.html',context=nothing)
def developers(request):
    # context_dict={'boldmessage': Courier.objects.all() }
    nothing = {}
    return render(request,'zoo/developers.html',context=nothing)
def tandc(request):
    # context_dict={'boldmessage': Courier.objects.all() }
    nothing = {}
    return render(request,'zoo/tandc.html',context=nothing)
