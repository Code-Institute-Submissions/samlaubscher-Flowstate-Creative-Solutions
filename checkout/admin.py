from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'date', 'order_total',
        'discount_total', 'grand_total',
    )

    fields = (
        'order_number', 'date', 'name',
        'username', 'email', 'discount_code',
        'order_total', 'discount_total', 
        'grand_total',
    )

    list_display = (
        'order_number', 'date', 'name',
        'order_total', 'discount_total', 
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
