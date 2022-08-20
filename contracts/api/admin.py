from django.contrib import admin

from .models import Claim, Client, Company, Contract, Manufacturer, Product, \
    Region, Shipment

admin.site.register(Claim)
admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Region)
admin.site.register(Shipment)
