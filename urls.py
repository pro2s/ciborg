from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djprj/', include('djprj.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    (r'^admin/(.*)', admin.site.root),
    (r'^dev_search/$', 'devices.views.dev_search'),
    (r'^$', 'devices.views.index'),
    (r'^service/$', 'devices.views.service'),
    (r'^contract/$', 'contracts.views.index'),  
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './images'}),
)
