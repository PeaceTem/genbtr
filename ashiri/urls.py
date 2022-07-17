"""ashiri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('leak-', include('leak.urls', namespace='leak')), # change the add share count ajax url if this path is changed
    path('ckeditor/', include('ckeditor_uploader.urls')), # r'^ckeditor/'
    path('src/', include('src.urls', namespace='src')),
    path('auth/', include('BTRauth.urls', namespace='auth')),
    path('draft/', include('draft.urls', namespace='draft')),
    path('archive/', include('archive.urls', namespace='archive')),
    path('@', include('genz.urls', namespace='genz')),

]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

