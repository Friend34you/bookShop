
# Register your models here.
from django.contrib import admin
from shop.models import Customer, Order, Book

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Book)
