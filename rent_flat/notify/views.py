from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Notification
from django.contrib import messages


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications.html'
    context_object_name = 'notifications'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(recipient=user)
        return queryset


class NotificationDetailView(LoginRequiredMixin, DetailView):
    model = Notification
    template_name = 'notification_detail.html'
    context_object_name = 'notification'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        Notification.objects.filter(pk=self.kwargs['pk']).update(unread=False)
        return queryset.filter(id=self.kwargs['pk'])