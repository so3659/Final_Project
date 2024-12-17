from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.http import JsonResponse


#added
from rest_framework import viewsets
from .serializers import PostSerializer
from django.utils import timezone


class BlogImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 


# Create your views here.
def js_test(request):
    return render(request, 'blog/js_test02.html', {})

def post_list(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not post.audio_file:
        post.generate_audio()
    return render(request, 'blog/post_detail.html', {'post': post})

def generate_audio(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.generate_audio()
    return JsonResponse({'audio_url': post.audio_file.url})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.image = request.POST['image']#form.Post.fields['image'] #form.DateField(input_formats=['blog_image/%Y/%m/%d/']) + request.POST['image']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.image = request.POST['image']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})