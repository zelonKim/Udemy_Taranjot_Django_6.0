from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Tag
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import CommentForm



def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    else:
        all_posts = Post.objects.all().order_by('-id')
        paginator = Paginator(all_posts, 3, orphans=1)
        page_number = request.GET.get('p', 2)
        page_obj = paginator.get_page(page_number)
        return render(request, 'posts/home.html', {'posts': page_obj})




def post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            posturl = reverse('post', args=[id])
            return HttpResponseRedirect(posturl)
        
    form = CommentForm()
    return render(request, 'posts/post.html', {'post_dict': post, 'form': form, 'comments': post.comment_set.all()})




def shortcut(request, id):
    url = reverse('find', args=[id])
    return HttpResponseRedirect(url)



def tags(request, id):
    tag = Tag.objects.get(id=id)
    return render(request, 'posts/tags.html', {'posts': tag.post_set.all()})