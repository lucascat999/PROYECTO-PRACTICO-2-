from django.db import models

class Persona(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    apellido = models.CharField(verbose_name="Apellido", max_length=50)
    edad = models.IntegerField(verbose_name="Edad")
    oficina = models.ForeignKey('oficina.Oficina', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def _str_(self):
        return f"{self.nombre} {self.apellido}"