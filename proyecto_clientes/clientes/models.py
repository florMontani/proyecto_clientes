from django.db import models

# Create your models here.
class Familia(models.Model):
    #charfil sirve para strings
    apellido = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.apellido
    
class Persona(models.Model):
    #charfil sirve para strings
    nombre = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True)
    familia_origen_id = models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.nombre}, {self.nacimiento}, id: {self.familia_origen_id}"
