from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.

def blog(request):
    allPosts = Post.objects.all()
    context ={'allposts':allPosts}
    return render (request,'htmlfile/blog.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug =slug)[0]
    context ={"post":post}
    return render (request,'htmlfile/blogpost.html',context)