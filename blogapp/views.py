from django.shortcuts import render, redirect
from blogapp.models import Blog
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q


def index(request):
    blog = Blog.objects.all()
    id = request.user.id
    users = User.objects.filter(~Q(id=id))
    context = {'Blogs': blog, 'Users': users}
    return render(request, 'index.html', context)

def likes(request, pk=None):
    user = request.user
    if user is None:
        return HttpResponse("Not logged in")
    
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponse("blod not exists")
    
    if user in blog.like.all():
        blog.like.remove(user) 
    else: 
        blog.like.add(user)

    blog.save()
    return redirect('index')
    
def make_friend(request, pk=None):
    user = request.user
    if user is None:
        return HttpResponse("Not logged in")
    
    return redirect('index')
    
