from django.contrib import admin
from .models import Customer, Item, Invoice

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Invoice)
