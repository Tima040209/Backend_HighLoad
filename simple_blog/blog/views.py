# blog/views.py

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from .models import Post
from django.core.cache import cache

@method_decorator(cache_page(60), name='dispatch')
class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'post_list.html', {'posts': posts})

def post_detail_view(request, post_id):
    post = Post.objects.select_related('author').prefetch_related('comments').get(id=post_id)
    recent_comments = cache.get(f'post_{post_id}_recent_comments')

    if not recent_comments:
        recent_comments = post.comments.all()[:5]
        cache.set(f'post_{post_id}_recent_comments', recent_comments, timeout=60)

    return render(request, 'post_detail.html', {'post': post, 'recent_comments': recent_comments})
