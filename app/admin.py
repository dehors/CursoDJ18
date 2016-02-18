from django.contrib import admin

# Register your models here.
from .models import SingUp
from .forms import SingUpForm
class PostModelSingUp(admin.ModelAdmin):
	list_display = ["__unicode__","updated","timestamp"] # campos a mostrar
	list_display_links = ["updated"] #campo link para editar
	#list_editable = ["email"]#campo editable
	list_filter = ["updated","timestamp"]#filtros de fechas en la parte derecha

	search_fields = ["__unicode__"]#buscador
	form = SingUpForm
	class Meta:
		model = SingUp

admin.site.register(SingUp, PostModelSingUp)