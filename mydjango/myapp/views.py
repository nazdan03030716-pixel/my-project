from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import PostForm, CommentForm

def home(request):
    posts = Post.objects.all()[:3]
    return render(request, 'myapp/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'myapp/publications.html', {'page_obj': page_obj})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    comment_list = post.comments.all().order_by('-created_at')
    paginator = Paginator(comment_list, 5)
    page_number = request.GET.get('page')
    comments = paginator.get_page(page_number)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('myapp:post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'myapp/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': form
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('myapp:post_list')
    else:
        form = PostForm()
    return render(request, 'myapp/post_form.html', {'form': form, 'title': 'Создать публикацию'})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('myapp:post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myapp/post_form.html', {'form': form, 'title': 'Редактировать'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:home')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})