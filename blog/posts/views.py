from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Post
from django.shortcuts import get_object_or_404

posts = [
    {
        'id': 1,
        'title': 'First Post',
        'content': 'This is the content of the first post.',
    },
    {
        'id': 2,
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
    },
    {
        'id': 3,
        'title': 'Third Post',
        'content': 'This is the content of the third post.',
    }
]


categories = [
    'Programming',
    'Food',
    'Travel',
]





def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    else:
        all_posts = Post.objects.all()
        print(all_posts)
        return render(request, 'posts/home.html', {'posts': all_posts, 'username': 'zelonKim', 'categories':categories})




def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post.html', {'post_dict': post})




def shortcut(request, id):
    url = reverse('find', args=[id])
    return HttpResponseRedirect(url)


