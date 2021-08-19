from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User




class Year(models.Model):
	user = models.ForeignKey(User, default=None)
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	# newcourse=models.ForeignKey(Course)
	# newbranch=models.ChainedForeignKey(
	# 	Branch,
	# 	chained_field="newcourse",
	# 	chained_model_field="course",
	# 	show_all=False
	# 	)
	code = models.CharField(max_length=10)
	# phone=models.CharField(max_length=30)
	ph=models.CharField(max_length=10)
	# year=models.CharField(max_length=10,choices=YEAR,default='1')
	# branch=models.CharField(max_length=40,choices=B_BRANCH,default='CSE')

	def __str__(self):
		return self.first_name