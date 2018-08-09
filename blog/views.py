from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from blog.models import Post
from blog.forms import PostNewForm


class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('created_date')
        return context


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'slug'
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, slug=self.kwargs['slug'])
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
            return redirect('blog:post_detail', slug=edit_post.slug)


@login_required
def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('blog:post_list')
