from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^prototype/$', views.prototype, name='prototype'),
    url(r'^accounts/invalid/$', 'warcraft.views.invalid_login'),
    url(r'^edit_name/$', views.edit_name, name='edit_name'),
]
