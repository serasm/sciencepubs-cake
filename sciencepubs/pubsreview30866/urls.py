from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.pubs_list, name='pubs_list'),
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
	url(r'^revlist$', views.review_list, name='review_list'),
    url(r'^pub/(?P<pub_id>[0-9]+)/$', views.pub_detail, name='pub_detail'),
    url(r'^pub/(?P<pub_id>[0-9]+)/add_review/$', views.add_review, name='add_review')
]