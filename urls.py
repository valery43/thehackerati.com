from django.conf.urls.defaults import *
import settings

from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
    (r'^about/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'about.html'}),
    (r'^agility/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'agility.html'}),
    (r'^contact/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'contact.html'}),
    (r'^culture/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'culture.html'}),
    (r'^custom/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'custom.html'}),
    (r'^engineering/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'engineering.html'}),
    (r'^innovation/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'innovation.html'}),
# Enable later, when users can apply for a job
#   (r'^join/$', 'django.views.generic.simple.direct_to_template',
#    {'template': 'join.html'}),
# Enable later
#   (r'^labs/$', 'django.views.generic.simple.direct_to_template',
#    {'template': 'labs.html'}),
    (r'^leadership/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'leadership.html'}),
    (r'^measurement/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'measurement.html'}),
    (r'^methodology/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'methodology.html'}),
# Enable later
#   (r'^partners/$', 'django.views.generic.simple.direct_to_template',
#    {'template': 'partners.html'}),
    (r'^people/$', 'github_org.views.index'),
    (r'^people/(?P<login>.*)$', 'github_org.views.profile'),
    (r'^product/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'product.html'}),
    (r'^research/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'research.html'}),
    (r'^team/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'team.html'}),
# Enable later, when users can apply for a job
#   (r'^terms/$', 'django.views.generic.simple.direct_to_template',
#    {'template': 'terms.html'}),
    (r'^value/$', 'django.views.generic.simple.direct_to_template',
     {'template': 'value.html'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
