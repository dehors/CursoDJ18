from django.contrib import admin

# Register your models here.
from .models import SingUp

class PostModelSingUp(admin.ModelAdmin):
	list_display = ["email","updated","timestamp"] # campos a mostrar
	list_display_links = ["updated"] #campo link para editar
	list_editable = ["email"]#campo editable
	list_filter = ["updated","timestamp"]#filtros de fechas en la parte derecha

	search_fields = ["email"]#buscador
	class Meta:
		model = SingUp

admin.site.register(SingUp, PostModelSingUp)