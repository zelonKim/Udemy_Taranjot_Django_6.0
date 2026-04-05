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
    all_posts = Post.objects.all()
    print(all_posts)
    return render(request, 'posts/home.html', {'posts': all_posts, 'username': 'zelonKim', 'categories':categories})



# def home(request, city):
#     print(reverse('basic', args=[city])) # /posts/home/busan
#     return render(request, 'posts/home.html', {'posts': posts, 'username': 'zelonKim'})




def post(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except:
    #     raise Http404()
    
    post = get_object_or_404(Post, id=id)
    
    return render(request, 'posts/post.html', {'post_dict': post})




# def post(request, id):
#     valid_id = False
    
#     for post in posts:
#         if post['id'] == id:
#             post_dict = post
#             valid_id = True
#             break
#     if valid_id:
#         html = f'''
#             <h1>{post_dict['title']}</h1>
#             <p>{post_dict['content']}</p>
#         '''
#         return HttpResponse(html)
#     else:
#         return HttpResponseNotFound("Post not available 😅")
#         raise Http404()
    
    
def shortcut(request, id):
    url = reverse('find', args=[id])
    return HttpResponseRedirect(url)

