from django.contrib import admin
from .models import User, Nivel
# Register your models here.

class NivelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nivel_usuario',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'pasword', 'email', 'cel',)
    search_fields = ('nombre','apellido','email',)
    list_filter = ('id_nivelU',)

admin.site.register(Nivel,NivelAdmin)
admin.site.register(User,UserAdmin)
