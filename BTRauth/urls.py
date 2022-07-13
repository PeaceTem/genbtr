from django.urls import path

from . import views

from django.contrib.auth.views import LogoutView
app_name= 'auth'

urlpatterns = [
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='auth:login'), name='logout'),


]