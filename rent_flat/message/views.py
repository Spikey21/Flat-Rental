from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat, Message
from .forms import ChatForm, MessageForm, MessageFormSet

User = get_user_model()


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['message_formset'] = MessageFormSet(self.request.POST)
        else:
            data['message_formset'] = MessageFormSet(queryset=Message.objects.none())
        return data

    @transaction.atomic
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
            # Save messages
            messages = message_formset.save(commit=False)
            for message in messages:
                message.chat = chat
                message.user = self.request.user  # Set the sender as the creator
                message.save()

            # transaction.set_autocommit(True)
            return redirect(self.success_url)

        else:
            return self.form_invalid(form)


class UserSuggestionsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
        results = [{'id': user.id, 'text': user.username} for user in users]
        return JsonResponse({'results': results})


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

