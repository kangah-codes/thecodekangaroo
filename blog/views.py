from django.shortcuts import render
from django.http import (
    HttpResponse
)
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def index(request):
    posts = BlogPost.objects.filter(is_featured=False)
    featured = BlogPost.objects.filter(is_featured=True)
    paginator = Paginator(posts, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": page_obj,
        "featured": featured
    }
    return render(request, 'index.html', context)

def tags(request):
    return render(request, 'index2.html')

def author(request):
    return render(request, 'author.html')

def post(request, post_slug):
    context = {
        "post": BlogPost.objects.get(slug=post_slug)
    }
    return render(request, 'port-color.html', context)