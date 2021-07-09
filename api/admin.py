from api.models import Cliente, ClienteHasGrupo, Grupo, Persona, Usuario
from django.contrib import admin

# Register your models here.
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Grupo)
admin.site.register(ClienteHasGrupo)