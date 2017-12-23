from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'articles/$', views.library_context, name='articles'),
]
