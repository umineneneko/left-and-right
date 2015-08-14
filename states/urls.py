from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^submit_comment$', views.create_comment, name='submit_comment'),
  url(r'^submit_state$', views.create_state, name='submit_state'),
]