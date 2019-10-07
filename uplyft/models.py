import datetime
from django.utils import timezone

from django.db import models
from django.forms import ModelForm, ModelChoiceField
#from django.forms import *

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

EMPLOYERS = [
    ('NYCZ', 'New York City Zoo'),
    ('NYCPD', 'New York City Police Department'),
]

OCCUPATIONS = [
    ('STUDENT', 'Student'), 
    ('FULL TIME', 'Full time employee'), 
    ('PART TIME', 'Part time employee'),
]

US_CITIES = [
     ('SPR', 'Springfield'), 
     ('NYC', 'New York City'), 
]

US_STATES = [
    ('NY', 'New York'), 
    ('NJ', 'New Jersey'),
]

YEARS_OF_EXPERIENCE = [
    ('0-1', '0 to 1 year'),
    ('2', '2 years'),
    ('3-5', '3-5 years'),
    ('5-10', '5-10 years'), 
    ('10+', '10+ years'),
]

class CandidateRegistrationModel(models.Model):
    first_name = models.CharField(
        max_length=60,
        null=False,
        blank=True,
        help_text="The candidate's first name.",
    )
    last_name = models.CharField(
        max_length=60,
        null=False,
        blank=True,
        help_text="The candidate's last name.",
    )
    email = models.EmailField(
        max_length=200,
        null=False,
        blank=True,
        help_text="The candidate's email address.",
    )
    password = models.CharField(
        max_length=200,
        null=False,
        blank=True,
        help_text="The candidate's password.",
    )
    password_retype = models.CharField(
        max_length=200,
        null=False,
        blank=True,
        help_text="The candidate's password, again.",
    )
    occupation = models.CharField(
        max_length=100,
        choices = OCCUPATIONS,
        null=False,
        #empty_label = "Pick an occupation type",
        help_text="The candidate's occupation.",
    )
    phone_number = models.CharField(
        null=False,
        #empty_label = "(212)-200-0000",
        max_length = 12, 
        help_text = "The candidate's phone number.",
        # @TODO https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    )
    address_line_1 = models.CharField(
        null=True, 
        #empty_label = "Street, Building Number",
        max_length = 200, 
        help_text = "The candidate's address (line 1).",
    )
    address_line_2 = models.CharField(
        null=True, 
        #empty_label = "",
        max_length = 200, 
        help_text = "Apartment/Unit Number",
    )
    city = models.CharField(
        max_length = 100, 
        choices = US_CITIES, 
        null = False,
        help_text = "The candidate's city.",
    )
    state = models.CharField(
        max_length = 100, 
        choices = US_STATES, 
        null = False,
        help_text = "The candidate's state.",
    )
    zipcode = models.CharField(
        max_length = 20,
        null=False, 
        help_text = "The candidate's zipcode.", 
    )
    skills = models.CharField( # Will need to become a dynamic number of text boxes
        max_length = 500, 
        null = False, 
        help_text = "The candidate's skills",
    )
    years_of_experience = models.CharField(
        max_length = 100, 
        choices = YEARS_OF_EXPERIENCE, 
        null = False, 
        help_text = "The candidate's number of years of employment experience.",
    )
    disability_form_upload = models.FileField(
        null = True, 
        max_length = 200, 
    )
    veteran_status_upload = models.FileField(
        null = True, 
        max_length = 200, 
    )
    resume_upload = models.FileField(
        null = True, 
        max_length = 200, 
    )
    photo_upload = models.FileField(
        null = True, 
        max_length = 200, 
    )

    def __str__(self):
        return self.first_name


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): #Add __str__() methods to models (https://docs.djangoproject.com/en/2.2/intro/tutorial02/)
    	return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text