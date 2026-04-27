from django.db import models

class SingletonModel(models.Model):
    class Meta:
        abstract= True
    def save(self, *args, **kwargs):
        self.pk=1
        super().save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        return {0, {}}
    @classmethod
    def load(cls, defaults = None):
        if defaults is None:
            defaults={}
        obj, created=cls.objects.get_or_create(pk=1)
        return obj