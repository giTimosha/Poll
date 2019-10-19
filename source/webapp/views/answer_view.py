from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.form import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceCreateAnswer(CreateView):
    template_name = 'answer/create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        poll.Poll.create(**form.cleaned_data)
        return redirect('poll_view', pk=poll_pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'answer/update.html'
    context_object_name = 'answer'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    context_object_name = 'answer'
    template_name = 'answer/delete.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})
