from django.db import models
class Product(models.Model):
    name = models.CharField("Nom du produit", max_length=200)
    price = models.PositiveIntegerField("Prix")
    description = models.TextField("Description")
    is_active = models.BooleanField("Actif", default=True)
    order = models.PositiveIntegerField("Ordre d'affichage")
    icon=models.CharField("Icône", max_length=50,blank=True,help_text="Emoji ou classe CSS")
    class Meta:
        abstract = True
        ordering = ["order", "name"]
    def __str__(self) -> str:
        return self.name