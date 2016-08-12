from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Post, Comment
from django.utils import timezone


def index(request):
    posts = Post.objects.all().order_by('-published_date')
    user = request.user
    context = {'posts':posts, 'user':user}
    return render(request, 'blog/index.html', context)
    
    
def write(request):
    post = Post()
    post.author = request.user
    post.title = request.POST['title']
    post.text = request.POST['text']
    post.published_date = timezone.now()
    post.save()
    return redirect('index')
    

def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.author = request.user
        post.title = request.POST['title']
        post.text = request.POST['content']
        post.published_date = timezone.now()
        post.save()
        return redirect('index')
    else:
        context={'post':post}
        return render(request, 'blog/post_edit.html', context)
        
        
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')
    
        
def reply_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('index')
    
    
def reply_write(request):
    comment = Comment()
    comment.post_id = request.POST['id_of_post']
    comment.author = request.user
    comment.text = request.POST['content']
    comment.save()
    return redirect('index')