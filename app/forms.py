from django import forms
from .models import SingUp

class SingUpForm(forms.ModelForm):
	class Meta:
		model = SingUp
		fields = [
			"email",
			"full_name",
		]
		exclude = ["full_name"]