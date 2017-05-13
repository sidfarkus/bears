from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^collections/new$', views.new_collection, name='new_collection'),
]