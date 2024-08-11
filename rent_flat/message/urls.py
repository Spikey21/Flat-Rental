from django.urls import path
from .views import ChatListView, ChatCreateView, ChatDetailView, MessageCreateView, UserSuggestionsView

urlpatterns = [
    path('messages', ChatListView.as_view(), name='chat_list'),
    path('messages/create/', ChatCreateView.as_view(), name='create_chat'),
    path('messages/<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),
    path('messages/<int:chat_id>/send/', MessageCreateView.as_view(), name='send_message'),
    path('user-suggestions/', UserSuggestionsView.as_view(), name='user_suggestions'),
]