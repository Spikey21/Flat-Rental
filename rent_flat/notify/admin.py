from django.contrib import admin

from .models import Notification, NotificationType


class NotificationTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("message", "recipient", "created_at", "unread")
    list_filter = ("message", "recipient", "created_at")
    search_fields = ("message", "recipient")
    ordering = ("created_at", "unread")


admin.site.register(NotificationType, NotificationTypeAdmin)