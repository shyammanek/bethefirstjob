from django.db import models

# Create your models here.
class joblist(models.Model):
    Companyname = models.CharField(max_length=1000)
    Experiance = models.CharField(max_length=1000)
    Jobtype = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    Link= models.CharField(max_length=1000)


    def __str__(self):
        return self.Companyname + " - " + self.Experiance
