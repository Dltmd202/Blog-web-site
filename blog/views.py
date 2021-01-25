from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'