from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Code(models.Model):
	user = models.ForeignKey(User, default=None)
	code=models.CharField(max_length=5)
