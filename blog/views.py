from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request):
    one_blog=Blog.objects
    return render(request,'home.html',{'blogs':one_blog})

def detail(request,blog_id):
    one_blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blogs':one_blog})

def new(request):
    return render(request,'new.html')

def create(req):
    one_blog=Blog()
    one_blog.title=req.POST['title']
    one_blog.body=req.POST['body']
    one_blog.pub_date=timezone.datetime.now()
    one_blog.save()
    return redirect('/detail/'+str(one_blog.id))

def delete(req,blog_id):
    one_blog=get_object_or_404(Blog,pk=blog_id)
    one_blog.delete()
    return redirect('/')

def portfolio(req):
    return render(req,'portfolio.html')