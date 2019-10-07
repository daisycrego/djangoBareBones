import datetime
from django.db import models
from django.utils import timezone

class RegistrationForm(models.Model):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	email_address = models.CharField(max_length=200)
	password = models.CharField(max_length=500)
	retype_password = models.CharField(max_length=500)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self): #Add __str__() methods to models (https://docs.djangoproject.com/en/2.2/intro/tutorial02/)
    	return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text