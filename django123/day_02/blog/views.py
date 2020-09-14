from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
import datetime
# Create your views here.
def home(request):
    # 리퀘스트라는 요청은 검색어를 입력해서 엔터를 했울떄 안보이는 과정에서 그 검색어에 관련된 키워드르 반환해서 보여달라는 요청 
    blog = Blog.objects.all()
    return render(request, "index.html", {'blog':blog})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "detail.html", {'blog':blog})

def new(request):
    return render(request, "new.html")

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.pub_date = datetime.datetime.now()
    blog.content = request.GET['content']
    blog.save()
    return redirect('/')
    # 동작이 끄ㅜㅌ나고 어떤 페이지를 보여줄건지 설정(메인 페이지로 설정할려면 슬래쉬)

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "update.html", {'blog':blog})

def updateAction(request, blog_id):
    # 해당하는 게시물의 내용을 수정해서 저장하는 액션이기대문에 어떠한 게시물을 수정할 것인지 정보가 있어야해서 blog_id 가 필요함
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.pub_date = datetime.datetime.now()
    blog.content = request.GET['content']
    blog.save()
    return redirect('/detail/' + str(blog_id))

def delete(request, blog_id):
    get_object_or_404(Blog, pk=blog_id).delete()
    return redirect('/')