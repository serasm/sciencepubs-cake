"""sciencepubs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from pubssearch30783.views import SearchList

urlpatterns = [
    path('', include('sciencepublications.urls')),
    path('excel/', include('excel30882.urls')),
    path('publicationview/', include('publicationview30890.urls')),
    path('admin/', admin.site.urls),
    path('detail/', include('detailView.urls')),
    path('pubssearch/', SearchList.as_view(), name="szukajka"),
]
