from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self) -> str:
        return self.nombre + " " + self.cedula + " " + self.nacimiento



