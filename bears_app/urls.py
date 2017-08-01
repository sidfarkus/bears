from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/new', views.new_user, name="new_user"),
    url(r'^collections/new$', views.new_collection, name='new_collection'),
    url(r'^collections/create$', views.create_collection, name='create_collection'),
]