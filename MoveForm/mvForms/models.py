from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.utils.translation import gettext as _
class moveForm(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=200)
    #userID = models.AutoField
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
       return self.fName

class mvForm(ModelForm):
    class Meta:
        model = moveForm
        fields = ['fName', 'lName', 'eMail', 'Citizenship','Company',
                  'Manager', 'subPOC', 'program', 'location', 'phoneNum', 'faaBadge', 'faaParking', 'comments']

class taskOverview(models.Model):
  person = models.ForeignKey(moveForm, on_delete=models.CASCADE)
  assignee = models.CharField(max_length = 200)
  completionDate = models.CharField(max_length = 200)
  taskToBeCompleted = models.CharField(max_length = 500)
    
class user(models.Model):
  firstName = models.CharField(max_length=100)
  lastName = models.CharField(max_length=200)
  eMail = models.CharField(max_length = 200)
  company = models.CharField(max_length = 200)
  Manager = models.CharField(max_length = 200)
  program = models.CharField(max_length = 200)
  phoneNum = models.IntegerField()