from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
	path("<int:PublicationId>", views.category, name="category"),
    ]