from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    available=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)

#Using modelforms class to create a model and a form at the same time
class Calendar(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=100)

class Contacts(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    role = models.CharField(max_length = 200)
    email = models.IntegerField()
    phone= models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.first_name
    
class Team(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    email = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name
    
class leaguetable(models.Model):
    teams=models.CharField(max_length=200)
    points=models.IntegerField()

    def __str__(self):
        self.teams
