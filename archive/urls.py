from django.urls import path

from . import views

app_name= 'archive'

urlpatterns = [
    path('leaks-archive/', views.LeaksArchive.as_view(), name='leaks-archive'),

]