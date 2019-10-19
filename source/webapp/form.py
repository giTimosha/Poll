from django import forms
# from django.forms import widgets
from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['questions']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['option_text']
