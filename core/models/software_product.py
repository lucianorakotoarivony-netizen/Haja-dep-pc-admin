from django.db import models
from .product import Product
from filer.fields.image import FilerImageField

class Software(Product):
    version=models.CharField("Version", max_length=200, blank=True)
    image=FilerImageField(blank=True, null=True, on_delete=models.SET_NULL, 
                           related_name="software_image" )
    image_url = models.CharField(max_length=255, blank=True, null=True, editable=True)
    def save(self, *args, **kwargs):
        if self.image:
            self.image_url=self.image.url
            super().save(*args,**kwargs)
    class Meta(Product.Meta):
        verbose_name="Logiciel"
        verbose_name_plural="Logiciels"