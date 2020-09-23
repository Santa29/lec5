from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post 
    template_name = 'home.html'
    context_object_name = 'posts_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'