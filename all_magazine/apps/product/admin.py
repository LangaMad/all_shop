from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(TestProduct)
class TestProductAdmin(admin.ModelAdmin):
    list_display = ['name','articul','price',
                    'description','image','is_active']


