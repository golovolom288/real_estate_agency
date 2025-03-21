from django.contrib import admin
from property.models import Flat, Report, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', "has_balcony", 'rooms_number')
    raw_id_fields = ('likes',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat",)
    list_display = ('flat', 'username', 'report')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)

