from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^download/$', index.download, name='download'),
]