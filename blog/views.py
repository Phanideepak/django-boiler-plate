from datetime import date
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse

from blog.forms import CommentForm
from .models import Post


def get_date(post):
    return post['date']

class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'

# class SinglePostView(DetailView):
#     template_name = 'blog/post-detail.html'
#     model = Post

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post_tags'] = self.object.tags.all()
#         context['comment_form'] = CommentForm()
#         return context


class SinglePostView(View):
    def is_stored_post(self, request, post_id):
       stored_posts = request.session.get('stored_posts')
       if stored_posts is not None:
           is_saved_for_later = post_id in stored_posts
       else:
           is_saved_for_later = False

       return is_saved_for_later 

    def get(self, request, slug):
       post =  Post.objects.get(slug = slug)
           
       context = {
           'post' : post,
           'post_tags' : post.tags.all(),
           'comment_form' : CommentForm(),
           'comments' : post.comments.all().order_by('-id'),
           'saved_for_later' : self.is_stored_post(request, post.id)
       }
       return render(request, 'blog/post-detail.html', context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug = slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_detail_page', args=[slug]))
        

        context = {
            'post' : post,
            'post_tags' : post.tags.all(),
            'comment_form' : comment_form,
            'comments' : post.comments.all().order_by('-id'),
            'saved_for_later' : self.is_stored_post(request, post.id)
        }
        
        return render(request, 'blog/post-detail.html', context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in = stored_posts)
            context['posts'] = posts
            context['has_posts'] = True
        
        return render(request, 'blog/stored-posts.html', context)


    def post(self, request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session['stored_posts'] = stored_posts
        else:
            stored_posts.remove(post_id)
        
        return HttpResponseRedirect('/blog/')







# Below methods are not attached to urls.py.
def starting_page(request):
    all_posts = Post.objects.all().order_by('-date')
    #sorted_posts = sorted(all_posts, key = get_date)
    latest_posts = all_posts[:3]
    return render(request, 'blog/index.html', {'posts' : latest_posts})

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', { 'all_posts' : all_posts })

def post_detail(request, slug):
    # identified_post = Post.objects.get(slug = slug)
    identified_post = get_object_or_404(Post, slug = slug)
    return render(request, 'blog/post-detail.html', {
        'post' : identified_post,
        'post_tags': identified_post.tags.all()
    })