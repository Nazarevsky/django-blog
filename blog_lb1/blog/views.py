from django.shortcuts import render, redirect
from .models import Post, Comment

from django.contrib.auth import authenticate, logout, login

from .models import Post

def home(request):
    data = {
        'posts': Post.objects.all(),
        'title':"Головна"
    }

    return render(request, 'home.html', data)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    
    data = {
        'post': post,
        'comments': post.comment_set.all().order_by('timestamp'),
        'title':"Перегляд посту",
        'user':request.user
    }
    if request.method == 'POST':
        if request.POST.get("comment_del"):
            Comment.objects.get(pk=request.POST.get('id')).delete()
            return redirect('post_detail', pk=pk)
        if request.POST.get("send_comment"):
            if request.POST.get('comment') != "" and request.POST.get('comment') is not None and len(request.POST.get('comment')) <= 250:
                Comment.objects.create(author=request.user, post=post, body=request.POST.get('comment'))
                return redirect('post_detail', pk=pk)
    
    return render(request, 'post_detail_single.html', data)

def exit(request):
    if request.user.is_authenticated:
        logout(request)

    data = {
        'posts': Post.objects.all()
    }

    return redirect("home")

def login_usr(request):
    error = ""
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "Невірний логін або пароль!"

    data = {
        'title':"Авторизація",
        'error':error
    }
    return render(request, 'login.html', data)