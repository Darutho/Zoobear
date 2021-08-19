from django.conf.urls import url 
from homez import views

urlpatterns = [ 
	url(r'^$',views.home, name='home'),
	url(r'^bookguide/',views.bookguide, name='bookguide'),
	url(r'^faq/',views.faq, name='faq'),
	url(r'^contact/',views.contact, name='contact'),
	url(r'^tutorial/',views.tutorial, name='tutorial'),
	url(r'^developers/',views.developers, name='developers'),
	url(r'^tandc/',views.tandc, name='tandc'),
	

	# url(r'^viewcourier/(?P<loc_from>[\w ]+)/(?P<loc_to>[\w ]+)/$',views.view_courier, name='view_courier'),
	# url(r'^viewcourier/(?P<loc_to>\w)/$', views.view_courier, name='view_courier'),
	# url(r'^request_made/$', views.req_made, name='req_made'),
]
