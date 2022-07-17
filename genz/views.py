from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from django.contrib.auth.mixins import LoginRequiredMixin


# from .forms import *

from django.contrib.auth.models import User
from .models import *



from  django.urls import reverse_lazy
# Create your views here.

# remove the login required mixin 
class HomePage(LoginRequiredMixin, View):

    def get(self, request, username):
        visitor = self.request.user
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        picture = profile.picture


        if not picture:
            picture = 'default'

        if visitor != user:
            profile.views += 1
            profile.save()

        context = {
            'user': user,
            'profile': profile,
            'visitor': visitor,
            'picture': picture,
        }
        return render(self.request, 'genz/profile.html', context)



