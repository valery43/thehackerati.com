from django.conf.urls.defaults import *
import settings

from django.contrib import admin
admin.autodiscover()

import github_org

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

# Simple page templates
urlpatterns += patterns('django.views.generic.simple',
    ('^$', 'direct_to_template', {'template': 'home.html'}),
    (r'^about/$', 'direct_to_template', {'template': 'about.html'}),
    (r'^agility/$', 'direct_to_template', {'template': 'agility.html'}),
    (r'^contact/$', 'direct_to_template', {'template': 'contact.html'}),
    (r'^culture/$', 'direct_to_template', {'template': 'culture.html'}),
    (r'^custom/$', 'direct_to_template', {'template': 'custom.html'}),
    (r'^engineering/$', 'direct_to_template', {'template': 'engineering.html'}),
    (r'^innovation/$', 'direct_to_template', {'template': 'innovation.html'}),
# Enable later, when users can apply for a job
#   (r'^join/$', 'direct_to_template', #    {'template': 'join.html'}),
# Enable later
#   (r'^labs/$', 'direct_to_template', #    {'template': 'labs.html'}),
    (r'^leadership/$', 'direct_to_template', {'template': 'leadership.html'}),
    (r'^measurement/$', 'direct_to_template', {'template': 'measurement.html'}),
    (r'^methodology/$', 'direct_to_template', {'template': 'methodology.html'}),
# Enable later
#   (r'^partners/$', 'direct_to_template', #    {'template': 'partners.html'}),
    (r'^product/$', 'direct_to_template', {'template': 'product.html'}),
    (r'^research/$', 'direct_to_template', {'template': 'research.html'}),
    (r'^team/$', 'direct_to_template', {'template': 'team.html'}),
# Enable later, when users can apply for a job
#   (r'^terms/$', 'direct_to_template', #    {'template': 'terms.html'}),
    (r'^value/$', 'direct_to_template', {'template': 'value.html'}),
)

urlpatterns += patterns('',
    url(r'^people/', include('github_org.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
