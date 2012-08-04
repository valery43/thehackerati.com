import datetime
from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.contrib.sites import *
from django.conf.urls.defaults import *

class ThehackeratiSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.6
    id = 2

    def items(self):
        return Site.objects.all()

    def lastmod(self, obj):
        return datetime.datetime.now()
    
class PeopleSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.6

    def items(self):
        from thehackerati_team import urls
        return [p for p in urls.urlpatterns if p.callback
                and p.callback.func_name == 'index']

    def lastmod(self, obj):
        return datetime.datetime.now()
    
    def location(self, obj):
        url = obj.regex.pattern.replace('^', '/people/').replace('$','')
        return url

class DirectToTemplateSitemap(Sitemap):
  changefreq = "daily"

  def __init__(self, patterns):
    self.patterns = patterns

  def items(self):
    return [p for p in self.patterns if p.callback 
               and p.callback.__module__ == 'django.views.generic.simple'
               and p.callback.func_name == 'direct_to_template']

  def changefreq(self, obj):
    return 'daily'

  def lastmod(self, obj):
    return datetime.datetime.now()

  def location(self, obj):
    url = obj.regex.pattern.replace('^', '/').replace('$','')
    return url