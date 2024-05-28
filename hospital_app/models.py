from django.db import models # type: ignore

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.IntegerField()
    special =models.CharField(max_length=50)


class Patient(models.Model):
    name=models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile =models.IntegerField()
    address = models.TextField()



class APPoiment(models.Model):
 doctor =models.ForeignKey(Doctor,on_delete=models.CASCADE)
 patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
 date = models.DateField()
 time = models.TimeField()