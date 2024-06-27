from django.urls import path
from .views import ChatListView, ChatCreateView, ChatDetailView, MessageCreateView

urlpatterns = [
    path('', ChatListView.as_view(), name='chat_list'),
    path('create/', ChatCreateView.as_view(), name='create_chat'),
    path('<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),
    path('<int:chat_id>/send/', MessageCreateView.as_view(), name='send_message'),
]