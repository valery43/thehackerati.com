from django.conf.urls.defaults import *
import settings

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
    (r'^about/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'about.html'}),
    (r'^contact/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'contact.html'}),
    (r'^terms/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'terms.html'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
