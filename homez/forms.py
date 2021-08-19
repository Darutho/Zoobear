import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class ComplaintForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=100)), label=_("Name"))
	feedback = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=100)), label=_("Subject"))
	details = forms.CharField(widget=forms.Textarea(attrs=dict(required=True, max_length=300)), label=_("Details"))
	