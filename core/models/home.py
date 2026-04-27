from django.db import models
from .mixin import SingletonModel
from django.core.validators import RegexValidator

class Home(SingletonModel):
    hex_color_validator = RegexValidator(
        regex=r'^#[0-9A-Fa-f]{6}$',
        message='Le format doit être #RRGGBB (ex: #FF5733)'
    )
    site_name = models.CharField("Nom du site", unique=True, default="Depannage PC")
    owner_name = models.CharField("Nom de propriétaire", unique=True, default="Your name")
    primary_color = models.CharField(
        "Couleur principale",
        default= "#000000",
        validators=[hex_color_validator],
        help_text="Format:#RRGGBB")
    class Meta(SingletonModel.Meta):
        verbose_name = "Accueil"
        verbose_name_plural= "Accueil"
    
    def __str__(self) -> str:
        return "Configuration de l'Accueil"
    @classmethod
    def load(cls):
        return super().load(defaults={
            'site_name': 'Depannage PC',
            'owner_name': 'Your name',
            'primary_color': '#000000'
        })