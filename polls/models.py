from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('问题', max_length=300)
    pub_date = models.DateTimeField('发布时间', default=timezone.now)

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项', max_length=300)
    votes = models.IntegerField('投票', default=0)
