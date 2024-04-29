from django.contrib import admin
from .models import CompanyBooking,Deal,Module3,Module4,Product,Trader

# Register your models here.

@admin.register(CompanyBooking)
class TranshipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CompanyBooking._meta.fields]


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Deal._meta.fields]


@admin.register(Module3)
class Module3Admin(admin.ModelAdmin):
    list_display = [field.name for field in Module3._meta.fields]


@admin.register(Module4)
class Module4Admin(admin.ModelAdmin):
    list_display = [field.name for field in Module4._meta.fields]



@admin.register(Product)
class Module4Admin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]



@admin.register(Trader)
class Module4Admin(admin.ModelAdmin):
    list_display = [field.name for field in Trader._meta.fields]