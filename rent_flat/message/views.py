from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat, Message
from .forms import ChatForm, MessageForm, MessageFormSet


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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['message_formset'] = MessageFormSet(self.request.POST)
        else:
            data['message_formset'] = MessageFormSet(queryset=Message.objects.none())
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        message_formset = context['message_formset']

        if form.is_valid() and message_formset.is_valid():
            # Create the Chat instance
            chat = form.save(commit=False)
            chat.admin = self.request.user
            chat.save()
            # Save the M2M relationships from the form
            form.save_m2m()
            # Add the creator to the participants
            chat.participants.add(self.request.user)
            # Debugging output after adding the creator
            print(f"After adding creator, participants are: {chat.participants.all()}")
            chat.save()

            # Save messages
            messages = message_formset.save(commit=False)
            for message in messages:
                message.chat = chat
                message.user = self.request.user  # Set the sender as the creator
                message.save()

            return super(ChatCreateView, self).form_valid(form)
        else:
            return self.form_invalid(form)



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

