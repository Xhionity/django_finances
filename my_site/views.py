from django.shortcuts import render
from django.db.models import Sum
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect, HttpResponseNotFound


def home(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Form is not correct'

    form = PostForm
    context = {
        'posts': Post.objects.all().order_by('-id'),
        'form': form,
        'error': error,
        'sum': Post.objects.aggregate(Sum('content'))
    }
    return render(request, 'my_site/home.html', context)


def edit(request, id):
    try:
        post = Post.objects.get(id=id)

        if request.method == "POST":
            post.title = request.POST.get("title")
            post.content = request.POST.get("content")
            post.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "my_site/edit.html", {"post": post})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect('/')
    except Post.DoesNotExist:
        return HttpResponseRedirect('<h2>Post not found</h2>')
