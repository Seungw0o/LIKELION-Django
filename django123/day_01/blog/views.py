from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
import datetime

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def temp(request):
    userid = request.GET['userid']
    password = request.GET['password']
    return render(request, 'temp.html', {'userid':userid, 'password':password})

def veiw(request):
    blog = Blog.objects.all()
    return render(request, 'view.html', {'blog':blog})

def detail(request, blog_id):
    obj = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'obj': obj})

def new(request):
    return render(request, "new.html")

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.pub_date = datetime.datetime.now()
    blog.content = request.GET['content']
    blog.save()
    return redirect('/view')

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'update.html')

def updateAction(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.pub_date = datetime.datetime.now()
    blog.content = request.GET['content']
    blog.save()
    return redirect('/view')

def delete(request, blog_id):
    get_object_or_404(Blog, pk=blog_id).delete()
    return redirect('/view')
    
