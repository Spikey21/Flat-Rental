from django.contrib import admin

from .models import Flat, FlatImage, Equip, FlatLocation, LocationCity


class FlatAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'price', 'status')
    list_filter = ("created_at", 'status')
    search_fields = ['title',]


class FlatImageAdmin(admin.ModelAdmin):
    list_display = ('flat',)
    list_filter = ('flat',)
    search_fields = ('flat',)


class LocationCityAdmin(admin.ModelAdmin):
    list_display = ('province', 'county', 'city')
    list_filter = ('province', 'county', 'city')
    search_fields = ['province', 'county', 'city']


class FlatLocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'street')
    list_filter = ('city', 'street')
    search_fields = ['city', 'street']


class EquipAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(FlatImage, FlatImageAdmin)
admin.site.register(Equip, EquipAdmin)
admin.site.register(LocationCity, LocationCityAdmin)
admin.site.register(FlatLocation, FlatLocationAdmin)
