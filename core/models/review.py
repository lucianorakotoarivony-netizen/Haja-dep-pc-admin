from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.functions import Now
class Review(models.Model):
    class Status(models.TextChoices):
        PENDING ='pending', 'En attente'
        APPROVED = 'approved', 'Approuvé'
        NOT_APPROVED = 'rejected', 'Rejeté'
    content = models.TextField(max_length=1000)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(db_default= Now(), db_column='createdAt')
    # Champs admin pour la modération. Nest ne fais que les lire. 
    is_active = models.BooleanField(default=True, db_default=True)
    core_status = models.CharField(
        max_length=20,
        choices=Status.choices,
        db_default=Status.PENDING,
    )

    # Relation avec User
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        db_column='userId'
    )
    class Meta:
        db_table='Review'
        verbose_name='Avis'
        verbose_name_plural = 'Avis'
    def __str__(self) -> str:
        return f"Avis de {self.user.username} - {self.rating}"

