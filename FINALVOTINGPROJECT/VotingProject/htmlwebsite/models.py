from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 200) 
    is_over = models.BooleanField(default=False)
    # pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    option = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.question} {self.option}"   

class ContactUs(models.Model):
    name = models.TextField()
    email = models.EmailField()
    message = models.TextField()

class Votes(models.Model):
    user = models.CharField(max_length=100)
    vote = models.BooleanField(default=False)