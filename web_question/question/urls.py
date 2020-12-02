from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('2', views.show_index, name='show_index'),
    path('', views.index, name='index'),
    url(r'^choice/(?P<pk>(\w)*)/$', views.choice, name='choice'),
    url(r'^exam$', views.exam, name='exam'),
    url(r'^e', views.show_exam, name='show_exam'),
    url(r'^f', views.show_fraction, name='show_fraction'),
]