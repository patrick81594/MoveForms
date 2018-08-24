from django.db import models
from django.utils import timezone


class moveForm(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=200)
    userID = models.CharField(max_length = 100)
    eMail = models.CharField(max_length = 200)
    citizenship = models.CharField(max_length = 100)
    company = models.CharField(max_length = 200)
    Manager = models.CharField(max_length = 200)
    subPOC = models.CharField(max_length = 200)
    program = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    phoneNum = models.IntegerField()
    faaBadge = models.CharField(max_length = 200)
    faaParking = models.CharField(max_length = 200)
    comments = models.CharField(max_length = 1000)
    publication_date = models.CharField(max_length = 50)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.fName

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