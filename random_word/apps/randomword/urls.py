from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^random_word/reset$', views.reset)
] 