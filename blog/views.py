from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from blog.models import Post, Tag
from blog.forms import PostNewForm, CommentForm


class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('created_date')
        context['tags'] = Tag.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'slug'
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, slug=self.kwargs['slug'])
        context['tags'] = Tag.objects.all()
        return context


@login_required
def post_new(request):
    if request.method != 'POST':
        form = PostNewForm()
        context = {'form': form}
        return render(request, 'blog/post_new.html', context)
    else:
        form = PostNewForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.publish()
            form.save_m2m()
            return redirect('blog:post_detail', slug=new_post.slug)


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method != 'POST':
        form = PostNewForm(instance=post)
        context = {'form': form, 'post': post}
        return render(request, 'blog/post_edit.html', context)
    else:
        form = PostNewForm(instance=post, data=request.POST)
        if form.is_valid():
            edit_post = form.save(commit=False)
            edit_post.author = request.user
            edit_post.publish()
            form.save_m2m()
            return redirect('blog:post_detail', slug=edit_post.slug)


@login_required
def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('blog:post_list')


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method != 'POST':
        form = CommentForm()
        context = {'form': form, 'post': post}
        return render(request, 'blog/add_comment.html', context)
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)


def tag_search_result(request, pk):
    posts = Post.objects.filter(tag__pk=pk)
    context = {'posts': posts, 'tags': Tag.objects.all()}
    return render(request, 'blog/tag_search_result.html', context)
