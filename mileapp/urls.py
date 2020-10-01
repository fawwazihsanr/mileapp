from django.conf.urls import url
from mileapp import views

urlpatterns = [
    url(r'^package$', views.get_package),
    url(r'^package/(?P<pk>[0-9]+)$', views.get_package_details),

]