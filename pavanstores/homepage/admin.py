from django.contrib import admin
from homepage.models import Foodgrain, Flour, Oil, Spice, Dryfruit, Masala, Order, OrderUpdate
# Register your models here.

admin.site.register(Foodgrain)
admin.site.register(Flour)
admin.site.register(Oil)
admin.site.register(Spice)
admin.site.register(Dryfruit)
admin.site.register(Masala)
admin.site.register(Order)
admin.site.register(OrderUpdate)