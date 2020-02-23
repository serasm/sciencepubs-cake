from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendrequest', views.sendRequest),
    path('import', views.ImportPublications)
]
