from django.conf.urls import url 
from books import views

urlpatterns = [ 
	url(r'^addbooks/', views.addbooks,name='addbooks'),
	url(r'^delete_books/', views.delete_books,name='delete_books'),
	url(r'^delete_book', views.delete_books,name='delete_books'),
	url(r'^buy_books', views.buy_books,name='buy_books'),
	url(r'^notif', views.notif,name='notif'),

]
