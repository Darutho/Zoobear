from django.conf.urls import url 
from login import views

urlpatterns = [ 
	# url(r'^login/',views.login, name='login'),
	url(r'^login/', 'django.contrib.auth.views.login'),
	url(r'^register/$', views.register,name='register'),
    url(r'^register/success/$', views.register_success,name='register_success'),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page,name='logout_page'),
    url(r'^home/$', views.home,name='home'),
	# url(r'^viewcourier/(?P<loc_from>[\w ]+)/(?P<loc_to>[\w ]+)/$',views.view_courier, name='view_courier'),
	# url(r'^viewcourier/(?P<loc_to>\w)/$', views.view_courier, name='view_courier'),
	# url(r'^request_made/$', views.req_made, name='req_made'),
]
