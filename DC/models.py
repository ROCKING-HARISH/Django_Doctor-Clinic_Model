from django.db import models

# Create your models here.


class Clinic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    founding_year = models.IntegerField()
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()

    def _str_(self):
        return self.name

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    experience = models.IntegerField()
    speciality = models.CharField(max_length=100)
    starttime = models.TimeField()
    endtime = models.TimeField()
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def _str_(self):
        return self.name 


