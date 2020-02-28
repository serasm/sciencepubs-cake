from django.conf.urls import url

from sciencepublications.views import (
    PublicationRudView,
    PublicationPostAPIView,
    CategoriesPostAPIView,
    CategoriesRudView
)

urlpatterns = [
    url(r'^publications/$', PublicationPostAPIView.as_view()),
    url(r'^publications/(?P<id>\d+)/$', PublicationRudView.as_view()),
    url(r'^categories/$', CategoriesPostAPIView.as_view()),
    url(r'^categories/(?P<id>\d+)/$', CategoriesRudView.as_view())
]