from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Comment
from django.utils import timezone

def home(request):
    return render(request, "firstapp/home.html")

def about(request):
    return render(request, "firstapp/about.html")

def career(request):
    return render(request, "firstapp/career.html")

def os(request):
    return render(request, "firstapp/study/os.html")

def dc(request):
    return render(request, "firstapp/study/dc.html")

def curriculum(request):
    return render(request, "firstapp/study/curriculum.html")

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    all_comments = post.comments.all().order_by('-created_at') #최신순 정렬
    return render(request, 'firstapp/detail.html', {'post' : post, 'comments':all_comments})

def post(request):
    posts = Post.objects.all()
    return render(request, "firstapp/post.html", {'posts':posts})


def new(request):
    return render(request, 'firstapp/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('firstapp:detail',new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id =id)
    return render(request, 'firstapp/edit.html', {'post': edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title=request.POST['title']
    update_post.writer=request.user
    update_post.pub_date=timezone.now()
    update_post.body = request.POST['body']
    if request.FILES.get('image'):
        update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('firstapp:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('firstapp:post')

def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, post=post)
    return redirect('firstapp:detail', post_id)

def edit_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.writer:
        return render(request, "firstapp/edit_comment.html", {"comment": comment})
    else:
        return redirect("firstapp:detail", comment.post.id)

def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.content = request.POST.get("content")
    comment.save()
    return redirect("firstapp:detail", comment.post.id)


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.writer:
        comment.delete()
    return redirect("firstapp:detail", comment.post.id)