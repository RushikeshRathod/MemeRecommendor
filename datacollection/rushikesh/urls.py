from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.default),
    url(r'^file', views.openxlms),
]
