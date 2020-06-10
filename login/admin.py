from django.contrib import admin
from .models import *
# Register your models here.

class NivelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nivel_usuario',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'cedula','cel','email','pasword',)
    search_fields = ('nombre','apellido','email',)
    list_filter = ('id_nivelU',)

class LoginAdmin(admin.ModelAdmin):
    list_display = ('id_nivelL', 'nombre_log', 'log', 'fecha_log')

admin.site.register(Nivel,NivelAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Login,LoginAdmin)
