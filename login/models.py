from django.db import models


# Create your models here.
class Nivel(models.Model):
    NIVELES = (
        ('Administrador', 'Administrador'),
        ('Cliente', 'Cliente'),
        ('Proyectos', 'Proyectos'),
        ('General', 'General'),
    )
    nivel_usuario = models.CharField(max_length=50, null=True, choices=NIVELES)
    
    def __str__(self):
        return self.nivel_usuario

class User(models.Model):
    nombre =  models.CharField(max_length=50)
    apellido = models.CharField(max_length=40)
    cedula = models.IntegerField(unique=True)
    cel = models.CharField(max_length=10)
    email = models.EmailField()
    id_nivelU = models.ForeignKey(Nivel, null=False, on_delete=models.CASCADE)
    pasword = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Login(models.Model):
    id_nivelL = models.ForeignKey(Nivel, null=False, on_delete=models.CASCADE)
    id_userL = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    nombre_log = models.CharField(max_length=50)
    apellido_log = models.CharField(max_length=50)
    log = models.BooleanField()
    fecha_log = models.DateTimeField(auto_now_add=True, null=True)