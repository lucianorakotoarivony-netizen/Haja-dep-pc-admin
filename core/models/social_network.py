from django.db import models

class SocialNetwork(models.Model):
    name = models.CharField("Nom", max_length = 50, default="")
    link = models.URLField("Lien", default="")
    icon = models.CharField("icône", help_text="Ex : logo-nom_du_site", default="")
    is_active = models.BooleanField("est actif", default = True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name= "Réseau social"
        verbose_name_plural = "Réseaux sociaux"
        ordering = ["order"]

    def __str__(self) -> str:
        return "Configuration des réseaux sociaux"

