from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('tags/', views.tags, name='tags'),
    path('blog/post/<slug:post_slug>', views.post, name='post'),
    path('author/', views.author, name='author'),
    path('tag/<str:obj>', views.tag_posts, name='tag_posts'),
    path('search/', views.search_query, name='search'),
    path('newsletter/', views.add_newsletter, name='newsletter')
]