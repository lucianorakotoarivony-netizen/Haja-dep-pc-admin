from django.db import models
from django.core.validators import MinValueValidator
class Service(models.Model):
    
    name=models.CharField("Nom du service", max_length=200, unique=True)
    description=models.TextField("Description")
    price=models.PositiveIntegerField("Prix", blank=True, null=True, help_text="Ex : 10000")
    icon=models.CharField("Icône", max_length=50,blank=True,help_text="Emoji ou classe CSS")
    order=models.IntegerField("Ordre d'affichage", default=0, validators=[MinValueValidator(0)])
    is_active=models.BooleanField("Active", default=True)

    class Meta:
        verbose_name="Service"
        verbose_name_plural="Services"
        ordering=["order","name"]
        
    def __str__(self) -> str:
            return self.name