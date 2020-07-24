from django.db import models
from django.db.models.signals import pre_save
from thecodekangaroo_django.util import *


# Create your models here.

# status for blog posts
BLOG_STATUS = (
	("DF", "Draft"),
	("PB", "Publish")
)

BLOG_COLORS = (
    ("red", "red"),
    ("blue", "blue"),
    ("green", "green"),
    ("orange", "orange"),
    ("violet", "violet"),
    ("empty", "empty"),
)

class Tag(models.Model):
    text = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    color = models.CharField(choices=BLOG_COLORS, blank=True, null=True, max_length=10)

    def __str__(self):
        return self.text

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now_add=True)
    banner = models.ImageField(null=True, blank=True)
    is_large = models.BooleanField()
    color = models.CharField(choices=BLOG_COLORS, max_length=10)
    status = models.CharField(choices=BLOG_STATUS, max_length=10)
    min_read = models.CharField(max_length=10)
    tags = models.ManyToManyField(Tag, related_name='+')
    slug = models.SlugField(null=True, blank=True)
    is_featured = models.BooleanField()

    def get_meta_image(self):
        if self.banner:
            return self.banner.url

    class Meta:
        db_table = "post"
        ordering = ['-post_date']
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/post/{self.slug}"

class Newsletter(models.Model):
    email = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"User {self.email}"

def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 

pre_save.connect(pre_save_receiver, sender=BlogPost)