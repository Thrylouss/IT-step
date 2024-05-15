from django.db import models

# Create your models here.


class Human(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

class Child(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    mother = models.OneToOneField(Human, related_name='mother', on_delete=models.SET_NULL, null=True)
    father = models.OneToOneField(Human, related_name='father', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class IceCream(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)
    customer = models.ForeignKey(Human, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()

    def __str__(self):
        return self.ice_cream.name
