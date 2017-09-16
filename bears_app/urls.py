from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^accounts/new', users.new, name="new_user"),
    url(r'^accounts/create$', users.create, name='create_user'),

    url(r'^$', collections.index, name='index'),
    url(r'^collections/new$', collections.new, name='new_collection'),
    url(r'^collections/create$', collections.create, name='create_collection'),
    url(r'^collections/show/(?P<id>[0-9]+)$', collections.show, name='show_collection'),
    url(r'^collections/add_song/(?P<id>[0-9]+)$', collections.add_song, name='add_song'),
]