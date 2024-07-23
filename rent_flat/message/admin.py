from django.contrib import admin

from .models import Chat, Message

# Register your models here.


class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'created',)
    list_filter = ('created', 'name')
    search_fields = ['name', 'participants',]


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'chat', 'timestamp',)
    list_filter = ("timestamp", 'user')
    search_fields = ['text', 'user']


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)