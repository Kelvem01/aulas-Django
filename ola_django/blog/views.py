from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404


# Create your views here.

def blog(request):
    context = {
        # 'text': 'Wellcome to My Blog',
        'posts': posts
    }
    return render(request,'home/home.html',context)

def post(request:HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    if found_post is None:
        raise Http404('Post not found')
    
    context = {
        
        'post': found_post
    }
    return render(request,'home/post.html',context)

def exemplo(request):
    context = {
        'text': 'Ola Exemplo ',
    }
    return render (request,'home/exemplo.html',context)
