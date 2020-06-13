from django import forms
from .models import User

class UserSignForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('user_name','user_mail','user_pass');

class UserLogForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('user_mail','user_pass');