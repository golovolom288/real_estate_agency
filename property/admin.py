from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner']


@admin.register(Flat)
class FlatModel(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ['town', 'address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintModel(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    raw_id_fields = ('flat',)


@admin.register(Owner)
class OwnerModel(admin.ModelAdmin):
    raw_id_fields = ('apartments',)