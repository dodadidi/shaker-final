from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #relationship 1:n (user:todos)
    dateCreated = models.DateField(auto_now_add=True) #automatic
    fullName = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    projectName = models.CharField(max_length=70)
    keyWord = models.CharField(max_length=70)
    description = models.TextField(blank=True) 
    imgUrl = models.FileField(upload_to='proj')
    fasion = models.BooleanField(default=False) #true or false
    art = models.BooleanField(default=False) #true or false
    chemical = models.BooleanField(default=False) #true or false
    jewellery = models.BooleanField(default=False) #true or false
    graphic = models.BooleanField(default=False) #true or false
    electronic = models.BooleanField(default=False) #true or false
    software = models.BooleanField(default=False) #true or false
    industrial = models.BooleanField(default=False) #true or false
    Textil  = models.BooleanField(default=False) #true or false

def __str__(self):
    return self.projectName


#from django.db import models
#from django.contrib.auth.models import User
## Create your models here.
#
#class Project(models.Model):
#    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #relationship 1:n (user:todos)
#    dateCreated = models.DateField(auto_now_add=True) #automatic
#    fullName = models.CharField(max_length=70)
#    email = models.CharField(max_length=70)
#    phone = models.CharField(max_length=10)
#    projectName = models.CharField(max_length=70)
#    keyWord = models.CharField(max_length=70)
#    description = models.TextField(blank=True)
#    image = models.FileField(upload_to='uploads/')
#
#
#def __str__(self):
#    return self.projectName
