from .models import Post
from django.views.generic import ListView , DetailView

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post