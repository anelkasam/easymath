from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'definitions/$', views.definitions, name='definitions'),
    url(r'subject/(?P<pk>\d+)$', views.subject, name='subject'),
    url(r'grade/(?P<pk>\d+)$', views.grade, name='grade'),
]
