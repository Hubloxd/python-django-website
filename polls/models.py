from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    q_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.q_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.c_text} -- {self.votes}"
