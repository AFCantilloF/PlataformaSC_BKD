from django.db import models

# Create your models here.
class Nivel(models.Model):
    nivel_usuario = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nivel_usuario

class User(models.Model):
    nombre =  models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    cel = models.CharField(max_length=10)
    pasword = models.CharField(max_length=20)
    id_nivelU = models.ForeignKey(Nivel, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return (self.nombre, self.pasword)