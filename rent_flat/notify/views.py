from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification
from django.contrib import messages

@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(recipient=request.user)
    messages.info(request, notifications)
    return render(request, 'notifications.html', {'notifications': notifications})