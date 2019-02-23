from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_file$', views.get_file, name='get_file'),
    url(r'^get_text$', views.get_text, name='get_text'),
]