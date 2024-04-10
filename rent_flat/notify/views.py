from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import Notification
from django.contrib import messages

@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(recipient=request.user)
    messages.info(request, notifications)
    return render(request, 'notifications.html', {'notifications': notifications})


class NotificationDetailView(LoginRequiredMixin, DetailView):
    model = Notification
    template_name = 'notification_detail.html'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        Notification.objects.filter(pk=self.kwargs['pk']).update(read=True)
        return queryset.filter(id=self.kwargs['pk'])