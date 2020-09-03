from django.contrib.sitemaps import Sitemap
from .models import BlogPost

class PostSiteMap(Sitemap):
	changefreq = 'weekly'
	priority = 0.8

	def items(self):
		return BlogPost.objects.filter(status="PB")

	def lastmod(self, obj):
		return obj.last_modified