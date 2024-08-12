from django.contrib import admin
from . models import *
# Register your models here.

# admin.site.register(Activity)
# admin.site.register(Department)
# admin.site.register(Order_Type)
admin.site.register(Buyer)
admin.site.register(Brand)
# admin.site.register(Season)
# admin.site.register(Drop)
# admin.site.register(Travel)
# admin.site.register(Employee)
# admin.site.register(Designation)
# admin.site.register(OTB)
# admin.site.register(Gender)
# admin.site.register(Fabric_Type)
# admin.site.register(Wwnww)
# admin.site.register(Domimp)
admin.site.register(Discussion)
admin.site.register(Details)
admin.site.register(Image)
admin.site.register(New_Order)
admin.site.register(OrderDetails)
admin.site.register(Pi)
admin.site.register(Pi_Item)
admin.site.register(Vendor)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','order_date','buyer','supplier','season','drop','created_on', 'modified_on']
admin.site.register(Order, OrderAdmin)
