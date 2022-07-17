from django.urls import path

from . import views

app_name= 'archive'

urlpatterns = [
    path('home/', views.HomePage.as_view(), name='home'),

    path('leaks-archive/', views.LeaksArchive.as_view(), name='leaks-archive'),
    path('add-leak/<int:leak_id>', views.AddLeak.as_view(), name='add-leak'),
    path('remove-leak/<int:leak_id>', views.RemoveLeak.as_view(), name='remove-leak'),


]