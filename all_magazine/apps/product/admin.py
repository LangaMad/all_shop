from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(TestProduct)
class TestProductAdmin(admin.ModelAdmin):
    list_display = ['name','articul','price','description','image','is_active']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'name',

    ]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name','brand','color','engine_type','drivers_location','drive_type','volume','year_manufacture','body','Country_origin']

@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',

    ]
    prepopulated_fields = {'slug': ('name',)}