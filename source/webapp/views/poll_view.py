from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.form import PollForm
from webapp.models import Poll
# from django.core.paginator import Paginator


class IndexView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'poll/index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    template_name = 'poll/view.html'
    context_key = 'polls'
    model = Poll


class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    context_object_name = 'poll'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    context_object_name = 'poll'
    template_name = 'poll/delete.html'

    def get_success_url(self):
        return reverse('index')
