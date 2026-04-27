from django.db import models
class User(models.Model):
    username = models.TextField(unique=True)
    email = models.TextField(unique=True)
    password = models.TextField()
    is_active = models.BooleanField(db_default=True)

    class Meta:
        managed = True
        db_table = 'User'
    def __str__(self) -> str:
        return self.username