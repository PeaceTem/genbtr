from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from .models import Archive
# Create your views here.
from leak.models import Leak

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'archive/home.html'
    redirect_field_name = 'next'

class LeaksArchive(LoginRequiredMixin, View):
    redirect_field_name = 'next'

    def get(self, request):
        archive = Archive.objects.prefetch_related('leaks').get(user=self.request.user)
        leaks = archive.leaks.all()
        pg = 'archive'
        context = {
            'leaks': leaks,
            'pg': pg,
        }


        return render(self.request, 'archive/leaks_archive.html', context)


class AddLeak(LoginRequiredMixin, View):
    redirect_field_name = 'next'

    def get(self, request, leak_id):
        user = self.request.user
        leak = Leak.objects.get(id=leak_id)
        archive = Archive.objects.get(user=user)
        archive.leaks.add(leak)
        return HttpResponse('added!')




class RemoveLeak(LoginRequiredMixin, View):
    redirect_field_name = 'next'

    def get(self, request, leak_id):
        user = self.request.user
        leak = Leak.objects.get(id=leak_id)
        archive = Archive.objects.prefetch_related('leaks').get(user=user)
        archive.leaks.remove(leak)
        return HttpResponse('removed!')






