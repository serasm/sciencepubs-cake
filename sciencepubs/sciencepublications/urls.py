from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    url(r'^api/sciencepublications/', include('sciencepublications.api.urls'))
]