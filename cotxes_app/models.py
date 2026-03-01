from django.db import models

# Taula 1: Marca
class Marca(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom de la Marca")
    pais = models.CharField(max_length=100, verbose_name="País d'origen")

    def __str__(self):
        return self.nom

# Taula 2: Model de Cotxe
class ModelCotxe(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom del Model")
    any_fabricacio = models.IntegerField(verbose_name="Any de fabricació")

    # LA RELACIÓ
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return f"{self.marca.nom} {self.nom} ({self.any_fabricacio})"
