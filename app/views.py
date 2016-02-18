from django.shortcuts import render
from .forms import SingUpForm
# Create your views here.

def home(request):
	title = "welcome"
	if request.user.is_authenticated():
		title = "My title %s" %(request.user)

	#print request
	#if request.method == "POST":
		#print request.POST
	form = SingUpForm(request.POST or None)#None desaparecer las validaciones
	if form.is_valid():
		instance = form.save(commit=False)# con el commit=False se devolvera un objeto que aun no se ha guardado, en este caso se debe de llamar el metodo save posteriormente
		full_name = form.cleaned_data.get("full_name")
		#print instance.timestamp
		if not full_name:
			instance.full_name = "Justin"
		instance.save()
		#print instance
		#print instance.email
		#print instance.timestamp
		context = {
			"title": "Success",
			"form": form,
		}		
		return render(request, "home.html", context)

	context = {
		"title": title,
		"form": form,
	}
	return render(request, "home.html", context)