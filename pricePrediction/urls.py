from django.conf.urls import patterns, url
import views
import api
from rest_framework.urlpatterns import format_suffix_patterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),

    url(r'^userSubmit', views.userSubmit, name="userSubmit"),

    url(r'^chrome', views.chrome, name="chrome"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # API
    url(r'^api/ads/$', api.CarAdList.as_view()),
    url(r'^api/ads/(?P<idFromSite>[0-9]+)/$', api.CarAdDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
