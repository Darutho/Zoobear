from django.conf.urls import url
from myprofile import views

urlpatterns = [
	url(r'^profile/', views.newprofile,name='newprofile'),
	url(r'^updatemyprofile/', views.updprofile,name='updprofile'),
	url(r'^otp/', views.otp,name='otp'),
]
