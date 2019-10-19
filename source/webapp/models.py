from django.db import models


class Poll(models.Model):
    questions = models.TextField(max_length=2000, verbose_name='вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.questions


class Choice(models.Model):
    option_text = models.TextField(max_length=2000, verbose_name='вариант текста')
    poll = models.ForeignKey('webapp.Poll', related_name='Poll', on_delete=models.CASCADE, verbose_name='опрос')

    def __str__(self):
        return self.option_text
