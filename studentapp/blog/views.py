from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_form.html', {'form': form})