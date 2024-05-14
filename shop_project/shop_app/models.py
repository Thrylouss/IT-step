from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    categorie = models.TextField(null=True)
    price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'furniture'
        verbose_name_plural = 'furnitures'
        ordering = ['id']
