from django.db import models
from .mixin import SingletonModel
from filer.fields.image import FilerImageField

class About(SingletonModel):
    title = models.CharField("Titre", max_length=200, default="Dépanneur")
    content = models.TextField("Contenu", default="Mon contenu")
    image = FilerImageField(blank=True, null=True , on_delete=models.SET_NULL, related_name="+")
    image_url = models.CharField(max_length=255, blank=True, null=True, editable=True)
    def save(self, *args, **kwargs):
        if self.image:
            self.image_url=self.image.url
            super().save(*args,**kwargs)

    class Meta(SingletonModel.Meta):
        verbose_name = "Page A propos"
        verbose_name_plural = "Page A propos"
    
    def __str__(self) -> str:
        return "Configuration A propos"
    @classmethod
    def load(cls):
        return super().load(defaults={
            "title": "Dépanneur",
            "content":"Mon contenu"
        })
    