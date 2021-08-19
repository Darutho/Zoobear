from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	auto_increment_id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User, default=None)
	book_name=models.CharField(max_length=100)
	author_name=models.CharField(max_length=100)
	subject=models.CharField(max_length=30)
	description=models.CharField(max_length=300)
	mrp=models.CharField(max_length=30)
	price=models.CharField(max_length=30)

	def __str__(self):
		return self.book_name 

class Notification(models.Model):
	auto_increment_id = models.AutoField(primary_key = True)
	to_user = models.ForeignKey(User, default=None)
	from_user = models.CharField(max_length=100)
	book_name=models.CharField(max_length=100)
	author_name=models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	# subject=models.CharField(max_length=30)
	# description=models.CharField(max_length=300)
	price=models.CharField(max_length=30)

	def __str__(self):
		return self.book_name 