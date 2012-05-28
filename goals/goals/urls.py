from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from goals import views

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.goals, name="home"),

    # Auth
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    (r'^accounts/$', 'django.views.generic.simple.redirect_to', {'url': '/'}),
    (r'^accounts/profile/$', 'django.views.generic.simple.redirect_to', {'url': '/'}),
    url(r'^logout$', 'django.contrib.auth.views.logout'),

    # API
    url(r'^api/check$', views.api_check),
)
