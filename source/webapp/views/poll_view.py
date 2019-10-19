from django.views.generic import ListView, DetailView

from webapp.models import Poll
# from django.core.paginator import Paginator


class IndexView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'poll/index.html'
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


class PollView(DetailView):
    template_name = 'poll/view.html'
    context_key = 'polls'
    model = Poll

