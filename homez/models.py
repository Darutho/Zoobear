from __future__ import unicode_literals

from django.db import models

# Create your models here.
class complaint(models.Model):
	name=models.CharField(max_length=100)
	feedback=models.CharField(max_length=100)
	details=models.CharField(max_length=300)

	def __str__(self):
		return self.name