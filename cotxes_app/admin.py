from django.contrib import admin
from .models import Marca, ModelCotxe

# Això fa que les taules apareguin al panell d'administració
admin.site.register(Marca)
admin.site.register(ModelCotxe)
