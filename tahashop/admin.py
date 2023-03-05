from django.contrib import admin
from . models import *
# Register your models here.


class AdminOrderItem(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity')
    

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem, AdminOrderItem)
admin.site.register(ShippingAddress)