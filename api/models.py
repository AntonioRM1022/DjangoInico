from django.db import models

# Create your models here.
class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)  # Corrigiendo el nombre de la variable 'usuairio_id' a 'usuario_id'
    nombre_usuario = models.CharField(max_length=255)

    class Meta:
        db_table = "usuarios"


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)  # Llave foránea a Usuarios

    class Meta:
        db_table = "genero"
