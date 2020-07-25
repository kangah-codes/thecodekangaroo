from django.shortcuts import render
from django.http import (
    HttpResponse
)
from django.core.paginator import Paginator
from .models import *
from simple_search import search_filter
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import JsonResponse


# Create your views here.
def index(request):
    posts = BlogPost.objects.filter(is_featured=False)
    featured = BlogPost.objects.filter(is_featured=True)
    paginator = Paginator(posts, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for post in posts:
        print(post.banner)
    context = {
        "posts": page_obj,
        "featured": featured,
        "tags": Tag.objects.all(),
        "ban": posts[0].banner
    }
    return render(request, 'index.html', context)

def tags(request):
    context = {
        "tags": Tag.objects.all()
    }
    return render(request, 'tags.html', context)

def tag_posts(request, obj):
    tagObj = Tag.objects.get(text=obj)
    context = {
        'posts': BlogPost.objects.filter(tags__text=obj),
        "tags": Tag.objects.all()
    }
    return render(request, 'index.html', context)

def author(request):
    context = {
        "tags": Tag.objects.all()
    }
    return render(request, 'author.html')

@csrf_exempt
def search_query(request):
    search_fields = ['^title', 'content']

    if request.method == "POST":
        posts = BlogPost.objects.filter(search_filter(search_fields, request.POST.get('query')))
        if len(posts) == 0:
            return HttpResponse(400)
        data = {}
        for post in posts:
            data[post.slug] = {
                "title":  post.title,
                "date": str(post.post_date)
            }
        return JsonResponse(data)

@csrf_exempt
def add_newsletter(request):
    if request.method == "POST":
        new_user = Newsletter(email=request.POST.get('email'))
        new_user.save()
        return HttpResponse(200)

def post(request, post_slug):
    context = {
        "post": BlogPost.objects.get(slug=post_slug),
        "tags": Tag.objects.all(),
        "link": 'http://'+request.META['HTTP_HOST']
    } 
    return render(request, 'post.html', context)

def handler404(request):
    return render(request, '404.html')


