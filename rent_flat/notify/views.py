from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView

from .models import Notification
from django.contrib import messages


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications.html'
    context_object_name = 'notifications'
    ordering = ['-created_at']

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(recipient=user)
        return queryset


class NotificationDetailView(LoginRequiredMixin, DetailView):
    model = Notification
    template_name = 'notification_detail.html'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        Notification.objects.filter(pk=self.kwargs['pk']).update(read=True)
        return queryset.filter(id=self.kwargs['pk'])