from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

def __str__(self):
    return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

def __str__(self):
    return self.choice_text

class Post(models.Model): 
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = ( 
    (Male, 'Male'), 
    (FeMale, 'Female'), 
    ) 

    Developer = 'Developer'
    Engineer = 'Engineer'
    PHPDeveloper = 'PHPDeveloper'
    POSITION_CHOICES = (
    (Developer, 'Developer'),
    (Engineer, 'Engineer'),
    (PHPDeveloper, 'PHPDeveloper')
    )
  
    # define a username filed with bound  max length it can have 
    username = models.CharField( max_length = 20, blank = False, 
                                 null = False) 

    position = models.CharField(max_length = 20, choices = POSITION_CHOICES, default = Developer) 

    # This is used to write a post 
    text = models.TextField(blank = False, null = False) 
      
    # Values for gender are restricted by giving choices 
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES,  
                              default = Male) 
      
    time = models.DateTimeField(auto_now_add = True) 

#creating custom field validation
def validate_G_mail(value): 
    if "@gmail.com" in value: 
        return value 
    else: 
        raise ValidationError("This field accepts mail id of google only") 

class GModel(models.Model):
    name = models.CharField( max_length = 20) 
    G_mail = models.CharField( max_length = 200, validators =[validate_G_mail]) 
    phone = models.IntegerField()


                        