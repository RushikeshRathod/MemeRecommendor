from django.conf.urls import url
from . import views

urlpatterns = [
    #/kartik/
    url(r'^$',views.index_kartik,name='index'),
    url(r'^add_data/',views.index_add_data_kartik,name='index'),
    url(r'^update_data/',views.update_kartik,name='update')
]