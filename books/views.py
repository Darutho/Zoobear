from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import BookForm
from .models import *
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from myprofile.models import Year


@csrf_protect

@login_required
def addbooks(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        # print "entered post"
        if form.is_valid():
            # print "form valid"
            # print "post variables", request.POST
            q=Book(user=request.user,book_name=form.cleaned_data['book_name'],author_name=form.cleaned_data['author_name'],subject=form.cleaned_data['subject'],price=form.cleaned_data['price'],description=form.cleaned_data['description'])
            q.save()

            # user = User.objects.create_user(
            # username=form.cleaned_data['username'],
            # password=form.cleaned_data['password1'],
            # email=form.cleaned_data['email']
            # )
            print "redirecting"
            return HttpResponseRedirect('/login/home')
        return render(request, 'books/errorbooks.html', {'form': BookForm})
    else:
        if Year.objects.filter(user=request.user):
            form = BookForm()
            user = request.user
            return render(request, 'books/addbooks.html', {'form': BookForm, 'user':user})
        else:
            return HttpResponseRedirect('/profile/profile')

@login_required
def delete_books(request):
    if request.method=='POST':
        print "post"
        checked = request.POST.getlist('cbook')
        for items in checked:
            for mi in Book.objects.filter(auto_increment_id=items):
                if Book.objects.filter(auto_increment_id=items).delete():
                    if Notification.objects.filter(to_user=request.user,book_name=mi.book_name).delete():
                        print "deleted"
        return HttpResponseRedirect('/login/home')
    else:
        if Book.objects.filter(user=request.user):
            dictc={'book':Book.objects.filter(user=request.user)}
            return render(request,'books/delete_books.html',context=dictc)
        else:
            nothing={}
            return render(request,'books/delete_books_error.html',context=nothing)


@login_required
def buy_books(request):
    if request.method=='POST':
        print "buying post"
        checked = request.POST.getlist('cbook')
        for items in checked:
            for mi in Book.objects.filter(auto_increment_id=items):
                print "buyingggggg"
                subject = 'Buyer Found!'
                subject2 = 'Book Requested'
                for jj in Year.objects.filter(user=request.user):
                    message = 'Hello '+str(mi.user.username)+'!!\nI am interested to buy the book- '+ str(mi.book_name)+' for Rs.'+ str(mi.price)+'. Please contact me on '+ str(jj.ph)+' or '+str(request.user.email)+'\nLooking forward for a reply!'
                    print "here now"
                    for kk in Year.objects.filter(user=mi.user):
                        print "here"
                        message2= 'Hello '+str(request.user)+'!! \n Your request to buy the book'+ str(mi.book_name)+ ' from ' + str(mi.user.username)+ ' for Rs.'+ str(mi.price)+' has been notified to him/her.They shall contact you soon or you can contact them on ' + str(kk.ph)+'\nCheers!\nZooBear'
                        q=Notification(to_user=mi.user,from_user=str(request.user),book_name=mi.book_name,author_name=mi.author_name,phone=jj.ph,price=mi.price)
                        q.save()
                        from_email = settings.EMAIL_HOST_USER
                        to_list =[mi.user.email]
                        to_list2=[request.user.email]
                        send_mail(subject,message,from_email,to_list,fail_silently = True)
                        send_mail(subject2,message2,from_email,to_list2,fail_silently = True)
                        print "mail sent"
        return HttpResponseRedirect('/login/home')



    else:
        if Year.objects.filter(user=request.user):
            dictc={'book':Book.objects.all()}
            # print dict
            return render(request,'books/buybooks.html',context=dictc)
        else:
            return HttpResponseRedirect('/profile/profile')


@login_required
def notif(request):
    if Notification.objects.filter(to_user=request.user):
        dictc={'notif':Notification.objects.filter(to_user=request.user)}
        return render(request,'books/notif.html',context=dictc)
    else:
        nothing={}
        return render(request,'books/notif_error.html',context=nothing)

