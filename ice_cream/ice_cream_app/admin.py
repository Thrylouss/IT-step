from django.contrib import admin
from .models import Human, Child, IceCream, Shop, Order

# Register your models here.
admin.site.register(Human)
admin.site.register(Child)
admin.site.register(IceCream)
admin.site.register(Shop)
admin.site.register(Order)
