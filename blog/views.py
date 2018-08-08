from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone


from .models import Post
from .forms import PostNewForm


class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('published_date')
        return context


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'slug'
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(slug=self.kwargs['slug'])
        return context


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
            return HttpResponseRedirect(reverse('blog:post_list'))
