from django.urls import path
from django.conf.urls import include, url
from . import views
from blog.sitemaps import PostSiteMap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "posts": PostSiteMap,
}

urlpatterns = [
	path('', views.index, name='index'),
    path('tags/', views.tags, name='tags'),
    path('blog/post/<slug:post_slug>', views.post, name='post'),
    path('author/', views.author, name='author'),
    path('tag/<str:obj>', views.tag_posts, name='tag_posts'),
    path('search/', views.search_query, name='search'),
    path('newsletter/', views.add_newsletter, name='newsletter'),
    path("blog/sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]