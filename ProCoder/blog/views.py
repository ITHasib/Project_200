from django.shortcuts import render, HttpResponse
from blog.models import Post


# Create your views here.

def blogHome(request):
    allpost= Post.objects.all()
    print(allpost)
    context= {'allpost': allpost}
    return render(request, "blog/blogHome.html", context)
    

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).fast()
    context = {'post':post}
    return render(request, "blog/blogPost.html", context)
