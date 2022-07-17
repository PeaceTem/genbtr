from django.urls import path

from . import views



app_name = 'genz'

urlpatterns = [
    path('<str:username>', views.HomePage.as_view(), name='profile'),
]
