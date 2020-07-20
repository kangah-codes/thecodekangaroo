from django.contrib import admin
from .forms import BlogForm
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
from .models import *

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	form = BlogForm
	field = "__all__"

myModels = [Newsletter, Tag]

admin.site.register(myModels, MarkdownxModelAdmin)
