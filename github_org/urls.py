from django.conf.urls.defaults import *

urlpatterns = patterns('github_org.views',
    url(r'^$', 'index'),
    url(r'^(?P<login>.*)$', 'profile'),
)
