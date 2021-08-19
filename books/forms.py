import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class BookForm(forms.Form):
	book_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=100)), label=_("Name of Book"))
	author_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=100)), label=_("Name of Author"))
	subject = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Subject (eg-PSCP,EM,BLE)"))
	description=forms.CharField(widget=forms.Textarea(attrs=dict(required=True, max_length=300)), label=_("Description/Condition"))
	price = forms.RegexField(regex=r'^\d+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Price"), error_messages={ 'invalid': _("numbers") })

