from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import View

from webapp.models import Poll, Choice, Answer


class PollAnswerView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choice = poll.Poll.all()
        context = {
            'poll': poll,
            'choices': choice
        }
        return render(request, 'output.html', context)

    def post(self, request, *args, **kwargs):
        pk = request.POST['answer']
        answer = get_object_or_404(Choice, pk=pk)
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        Answer.objects.create(pos_answer=answer, poll=poll)
        return redirect('index')
