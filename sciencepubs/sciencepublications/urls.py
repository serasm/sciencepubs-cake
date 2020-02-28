from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^api/sciencepublications/', include('sciencepublications.api.urls'))
]