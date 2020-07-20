from django.contrib import admin
from django.db import models
from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import BlogPost

class BlogForm(forms.ModelForm):
	content = forms.CharField(widget=AdminPagedownWidget())

	class Meta:
		model = BlogPost
		fields = "__all__"

