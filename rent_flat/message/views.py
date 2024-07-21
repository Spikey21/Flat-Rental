from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat, Message
from .forms import ChatForm, MessageForm


class ChatListView(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'chat/messages_list.html'

    def get_queryset(self):
        return self.request.user.chats.all()


class ChatCreateView(LoginRequiredMixin, CreateView):
    model = Chat
    form_class = ChatForm
    template_name = 'chat/messages_form.html'
    success_url = reverse_lazy('chat_list')


class ChatDetailView(LoginRequiredMixin, DetailView):
    model = Chat
    template_name = 'chat/messages_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'chat/message_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.chat_id = self.kwargs['chat_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('chat_detail', kwargs={'pk': self.kwargs['chat_id']})

