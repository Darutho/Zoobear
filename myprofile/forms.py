import re
from django import forms
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from login.models import Code
from django.core.cache import cache
class ProfileForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("First Name"))
	last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs=dict(required=True, max_length=30)))
	# course = forms.CharField(max_length=5,
	# 						widget=forms.Select(choices=COURSE))
	# year = forms.CharField(max_length=5,label=_("YEAR"),
	# 						widget=forms.Select(choices=YEAR,attrs={'size':1, 'required':True,'class':'special','padding':5}))
	# phone = forms.CharField(widget=forms.TextInput(attrs=dict(required=True)), label=_("Phone"),max_length=10)
	ph= forms.RegexField(regex=r'^\d+$', widget=forms.TextInput(attrs=dict(required=True, max_length=10)), label=_("Phone"), error_messages={ 'invalid': _("This value must contain numbers") })
	code= forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=4)),label=_("Verification Code"))
	# branch = forms.CharField(max_length=40,
	# 						widget=forms.Select(choices=B_BRANCH))

	# def __init__(self, user, *args, **kwargs):
	# 	self.user = user
	# 	super(ProfileForm, self).__init__(*args, **kwargs)
	
	def clean_ph(self):
		print "entered cleaning"
		if 'ph' in self.cleaned_data:
			if len(self.cleaned_data['ph']) != 10:
				print "u fucked up"
				raise forms.ValidationError(_("Enter 10 digits"))
		return self.cleaned_data['ph']
	def clean_code(self):
			# user = User.objects.get(username__iexact=self.cleaned_data['username'])
		# for items in Code.objects.filter(user=request.user):

			code_clean=cache.get('mob')
			print "cache code"
			print code_clean
			print "code of user"
			if 'code' in self.cleaned_data:
				print self.cleaned_data['code']
				if self.cleaned_data['code'] != str(code_clean):
					print "wrong code"
					raise forms.ValidationError(_("Wrong verification code"))

class ProfileForm2(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("First Name"))
	last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs=dict(required=True, max_length=30)))
	ph= forms.RegexField(regex=r'^\d+$', widget=forms.TextInput(attrs=dict(required=True, max_length=10)), label=_("Phone"), error_messages={ 'invalid': _("This value must contain numbers") })
	
	def clean_ph(self):
		print "entered cleaning"
		if 'ph' in self.cleaned_data:
			if len(self.cleaned_data['ph']) != 10:
				print "u fucked up"
				raise forms.ValidationError(_("Enter 10 digits"))
		return self.cleaned_data['ph']

