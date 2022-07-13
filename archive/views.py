from django.shortcuts import render, redirect

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from .models import Archive
# Create your views here.


class LeaksArchive(LoginRequiredMixin, View):

    def get(self, request):
        archive = Archive.objects.prefetch_related('leaks').get(user=self.request.user)
        leaks = archive.leaks.all()
        context = {
            'leaks': leaks,
        }

        return render(self.request, 'archive/leaks_archive.html', context)