from django.db import models


class Question_level(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Question_type(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Question(models.Model):
    question_type = models.ForeignKey(Question_type)
    question_level = models.ForeignKey(Question_level)
    stem = models.TextField()
    active = models.BooleanField()

class Answer(models.Model):
    answer_text = models.TextField()
    correct = models.BooleanField()
