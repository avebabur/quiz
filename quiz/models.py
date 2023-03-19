from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.CharField(max_length=2000)
    def __str__(self):
        return self.question
    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    answer = models.CharField(max_length=9999)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return f'question: {self.question.question}, answer: {self.answer}, correct: {self.correct}'


class Stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    overall = models.IntegerField()
    correct = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = 'Stat'
        verbose_name_plural = 'Stats'

class Flag(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    on_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.TextField()