from django.shortcuts import render
from .models import Post
from .forms import PostForm


def home(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'

    form = PostForm
    context = {
        'posts': Post.objects.all(),
        'form': form,
        'error': error
    }
    return render(request, 'my_site/home.html', context)
