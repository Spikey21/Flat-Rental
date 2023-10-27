from django.contrib import admin

from .models import Flat, FlatImage, Equip, FlatLocation


class FlatAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'price', 'location', 'status')
    list_filter = ("created_at", 'location', 'status')
    search_fields = ['title', 'location']


class FlatImageAdmin(admin.ModelAdmin):
    list_display = ('flat',)
    list_filter = ('flat',)
    search_fields = ('flat',)


class FlatLocationAdmin(admin.ModelAdmin):
    list_display = ('province', 'city')
    list_filter = ('province', 'city')
    search_fields = ['province', 'city']


class EquipAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(FlatImage, FlatImageAdmin)
admin.site.register(Equip, EquipAdmin)
admin.site.register(FlatLocation, FlatLocationAdmin)
