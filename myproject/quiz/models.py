from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    personality_type = models.CharField(max_length=50)  # e.g., introvert, extrovert, etc.

    def __str__(self):
        return self.text
