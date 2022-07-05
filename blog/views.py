from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
# from django.views.generic.edit import FormView
from django.views import View
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.db.models import Count

from .models import Post, Comment, AboutUs, PostView, Like
from .forms import PostForm, CommentForm


def post_list(request):
    



    # ordering = request.GET.get('ordering' ,'newer')

    # if ordering == 'newer':
        
    #     # posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date')
    #     sort = '-published_date'
        

    # # posts = Post.objects.filter(name__contains=ordering)
    # elif ordering == 'older':

    #     # posts = Post.objects.filter(published_date__isnull=False).order_by('created_date')
    #     sort = 'published_date'
    #     posts = Post.objects.filter(published_date__isnull=False).order_by(sort)

    # else:
    #     posts = Post.objects.all()

    

    # types = request.GET.get('types', 'published')

    # if types == 'published':

    #     # posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date')
        
    #     posts = Post.objects.filter(published_date__isnull=False).order_by(sort)

    # elif types == 'draft':

    #     # posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
        
    #     posts = Post.objects.filter(published_date__isnull=True).order_by(sort)

    # else:

    #     posts = Post.objects.all()

    ordering = request.GET.get('ordering' ,'newer')
    sort = '-published_date' if ordering == 'newer' else 'published_date'
    types = request.GET.get('types', 'published')
    posts = Post.objects.all().annotate(comments_count=Count('comments'))
    if type == 'published':
        posts.filter(published_date__isnull=False)
    else:
        posts.filter(published_date__isnull=True)

    return render(request, 'blog/post_list.html', {'posts': posts.order_by(sort)})
    


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # if not PostView.objects.filter(post_id=pk, user_id=request.user.id).exists():
    #     PostView.objects.create(post_id=pk, user_id=request.user.id)
    obj, created=PostView.objects.get_or_create(post_id=pk, user_id=request.user.id)
    return render(request, 'blog/post_detail.html', {'post': post})



# @login_required
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
   
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()

#             return redirect('blog:post_detail', pk=post.pk)
#     else:
#         form = PostForm()

#     return render(request, 'blog/post_edit.html', {'form': form})



@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})



@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date') 

    return render(request, 'blog/post_draft_list.html', {'posts': posts})



@login_required
def post_publish(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)




@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')



@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog:post_detail', pk=post.pk)

    else:
        form = CommentForm()

    return render(request, 'blog/add_comment_to_post.html', {'form': form})





@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)

    

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:post_detail', pk=comment.post.pk)




class About_Us(ListView):
    
    model = AboutUs
    context_object_name = 'about_us'
    queryset = AboutUs.objects.all()
    template_name = 'blog/about_us.html'




class CreatePostView(LoginRequiredMixin, View):
    
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    context_object_name = 'posts'

    def get(self, request, *args, **kwargs):
	    form = self.form_class
	    return render(request, self.template_name, {'form': form})



    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)




@login_required
def liked(request, pk):

    post = Post.objects.get(pk=pk)

    already_liked = Like.objects.filter(post=post, user=request.user)

    if not already_liked:
        liked_post = Like(post=post, user=request.user)
        liked_post.save()

        return redirect('blog:post_list')



@login_required
def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)

    already_liked.delete()
    already_liked.save()
    
    return redirect('blog:post_list')






