from django.urls import path
from . import views

app_name = 'src'


urlpatterns = [
    path('offline', views.OfflinePage.as_view(), name='offline'),
]