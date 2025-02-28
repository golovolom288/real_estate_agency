from django.contrib import admin
from property.models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')


admin.site.register(Flat, FlatAdmin)
