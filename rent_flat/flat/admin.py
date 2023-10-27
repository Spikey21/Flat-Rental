from django.contrib import admin

from .models import Flat, FlatImage


class FlatAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'price', 'location', 'status')
    list_filter = ("created_at", 'location', 'status')
    search_fields = ['title', 'location']


class FlatImageAdmin(admin.ModelAdmin):
    list_display = ('flat',)
    list_filter = ('flat',)
    search_fields = ('flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(FlatImage, FlatImageAdmin)
