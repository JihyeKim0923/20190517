from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request, 'diary/home.html', {'posts':posts})

def detail(request, post_id):
    detail=get_object_or_404(Post, pk=post_id)
    return render(request, 'diary/detail.html',{'post':detail,})

def new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.published_date=timezone.datetime.now()
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form=PostForm()
    return render(request,'diary/new.html',{'form':form})
    

def edit(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    if request.method=="POST":
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.published_date=timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.id)
    else:
        form=PostForm(instance=post)
    return render(request,'diary/edit.html',{'form':form, 'post':post})
    

def delete(request,post_id):
    post= get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home')     