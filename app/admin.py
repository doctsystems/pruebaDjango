from django.contrib import admin

# Register your models here.
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["email", "nombre", "timestamp"]
	list_editable = ["nombre"]
	class Meta:
		model = Registrado

admin.site.register(Registrado, AdminRegistrado)

