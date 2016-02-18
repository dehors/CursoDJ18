from django import forms
from .models import SingUp

class SingUpForm(forms.ModelForm):
	class Meta:
		model = SingUp
		fields = [
			"email",
			"full_name",
		]
		#exclude = ["full_name"]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain == 'USC':
			raise forms.ValidationError("ingrese un correo de USC")
		if not extension == "edu":
			raise forms.ValidationError("Porfavor ingrese una direccion de correo valida ")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name