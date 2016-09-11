from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>\d+)/fetchuserdetails/$', views.get_user, name='get_user'),
    url(r'^(?P<user_id>\d+)/getDonorCardDetails/$', views.get_donor, name='get_donor'),
    url(r'^(?P<user_id>\d+)/getDonations/$', views.get_donations, name='get_donations'),
    url(r'^(?P<user_id>\d+)/getRequests/$', views.get_requests, name='get_requests'),
    url(r'^(?P<request_id>\d+)/getRequest/$', views.get_request, name='get_request'),

]
