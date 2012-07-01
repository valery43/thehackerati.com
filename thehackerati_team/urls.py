from django.conf.urls.defaults import *

urlpatterns = patterns('thehackerati_team.views',
# Enable later, when users can apply for a job
#   (r'^join/$', 'direct_to_template', #    {'template': 'join.html'}),
    url(r'^$', 'index'),
    url(r'^(?P<login>.*)$', 'profile'),
)
