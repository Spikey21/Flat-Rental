from django.urls import path
from .views import ChatListView, ChatCreateView, ChatDetailView, MessageCreateView

urlpatterns = [
    path('chat-list', ChatListView.as_view(), name='chat_list'),
    path('chat-list/create/', ChatCreateView.as_view(), name='create_chat'),
    path('chat-list/<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),
    path('chat-list/<int:chat_id>/send/', MessageCreateView.as_view(), name='send_message'),
]