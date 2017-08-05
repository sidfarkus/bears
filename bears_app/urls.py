from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^accounts/new', users.new, name="new_user"),
    url(r'^accounts/create$', users.create, name='create_user'),

    url(r'^$', collections.index, name='index'),
    url(r'^collections/new$', collections.new, name='new_collection'),
    url(r'^collections/create$', collections.create, name='create_collection'),
]