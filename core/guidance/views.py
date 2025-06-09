# accounts/views.py
from django.shortcuts import render , get_object_or_404
from .models import RegistrationAnnouncement


def announcements_list(request):
    announcements = RegistrationAnnouncement.objects.filter(is_active=True).order_by('-published_at')[::-1]
    return render(request, "guidance/total_list.html", {"announcements": announcements})


def announcement_detail(request, pk):
    announcement = get_object_or_404(RegistrationAnnouncement, pk=pk, is_active=True)
    return render(request, "guidance/detail.html", {"announcement": announcement})