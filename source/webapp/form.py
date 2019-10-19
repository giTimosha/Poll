from django import forms
# from django.forms import widgets
from webapp.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['questions']
