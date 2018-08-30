from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.shortcuts import get_object_or_404

class moveForm(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=200)
    userID = models.AutoField
    eMail = models.EmailField()
    Citizenship = models.CharField(max_length = 100)
    Company = models.CharField(max_length = 200)
    Manager = models.CharField(max_length = 200)
    subPOC = models.CharField(max_length = 200)
    program = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    phoneNum = models.IntegerField()
    faaBadge = models.CharField(max_length = 200)
    faaParking = models.CharField(max_length = 200)
    comments = models.TextField(max_length = 1500)
    publication_date = models.DateTimeField()
    def was_published_recently(self):
       return self.publication_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
       return self.First_Name

class assignedTask(models.Model):
  assignee_choices = (
            ('patrick', 'Patrick'),
            ('david', 'David'),
            ('sean', 'Sean'),
            ('michelle','Michelle'),
            ('barbra', 'Barbra')
            )
  relatedForm = models.ForeignKey(moveForm, on_delete=models.CASCADE)
  assignee = models.CharField(max_length = 200)
  task = models.TextField()
  dateDue = models.DateTimeField()
  dateAssigned = models.DateTimeField(auto_now_add = True)
  assignedTo = models.CharField(max_length = 20, choices = assignee_choices, default = 'patrick')
        
  def __str__(self):
      mvFormDetails = get_object_or_404(moveForm, pk = self.pk)
      name = mvFormDetails.First_Name
      return name



class mvForm(ModelForm):
    class Meta:
        model = moveForm
        fields = ['First_Name', 'Last_Name', 'eMail', 'Citizenship','Company',
                  'Manager', 'subPOC', 'program', 'location', 'phoneNum', 'faaBadge', 'faaParking','publication_date', 'comments']

    
class user(models.Model):
  username_validator = ASCIIUsernameValidator()
  firstName = models.CharField(max_length=100)
  lastName = models.CharField(max_length=200)
  username = models.CharField(max_length= 100, default = "")
  eMail = models.CharField(max_length = 200)
  company = models.CharField(max_length = 200)
  Manager = models.CharField(max_length = 200)
  program = models.CharField(max_length = 200)
  phoneNum = models.IntegerField()

class userForm(ModelForm):
    class Meta:
        model = user
        
        fields = ['firstName', 'lastName', 'eMail', 'username',
                  'company', 'Manager', 'program', 'phoneNum']