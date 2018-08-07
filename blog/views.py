from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 100
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('date_added')
        return context


class PostDetailView(DetailView):
    model = Post

    # pass the url post_id to the class so query can be done.
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['slug'])
        return context
