from django.db import models
from .mixin import SingletonModel
from django.core.validators import RegexValidator

class Contact(SingletonModel):
    MESSAGE="Le numéro doit contenir exactement 10 chiffres (0355555555)"
    phone_validator=RegexValidator(regex=r'^0\d{9}$', message=MESSAGE)
    phone=models.CharField(
        "Téléphone", 
        max_length=10, 
        help_text=MESSAGE, 
        validators=[phone_validator], 
        default="0123456789")
    email=models.EmailField("Email", default="contact@dev.com")

    def __str__(self) -> str:
        return "Configuration des contacts"
    @classmethod
    def load(cls):
        return super().load(defaults={
            'phone': '0123456789',
            'email': 'contact@depanneur.com',
        })
    class Meta(SingletonModel.Meta):
        verbose_name="Contact"
        verbose_name_plural="Contacts"
    