from django.shortcuts import render, redirect

# function based views
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

# user registration form
class RegisterPage(FormView):
    template_name = 'BTRauth/register.html'
    form_class = CustomUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('leak:home')
    
        
    def form_valid(self, form):
        # form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')

        User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        user = authenticate(self.request, username=username, password=password)
        messages.success(self.request, f"You are logged in as {username}")
        login(self.request, user)

        return super(RegisterPage, self).form_valid(form)


    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.success(self.request, f"{self.request.user}, you've already registered!")
            return redirect('leak:home')
        
        return super(RegisterPage, self).get(request, *args, **kwargs)







class CustomLoginView(LoginView):
    template_name = 'BTRauth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('leak:home')