from django.conf.urls import url
from my_app import views

app_name = 'my_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),


]