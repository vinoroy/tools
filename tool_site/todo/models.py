from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Todo(models.Model):


    priorityChoices = (
        ('1', 'P1'),
        ('2', 'P2'),
        ('3', 'P3'),
    )


    statusChoices = (
        ('ND', 'Non débuté'),
        ('EC', 'En cours'),
        ('T', 'Terminé'),
    )

    category = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    dateCreated = models.DateField(auto_now_add=True,null=True, blank=True)
    priority = models.CharField(max_length=3, choices=priorityChoices, default='1')
    status = models.CharField(max_length=10,choices=statusChoices,default='ND')
    description = models.CharField(max_length=100,default='',null=True,blank=True)
    timeSpent = models.FloatField(null=True,blank=True,default=None)
    distance = models.FloatField(null=True,blank=True,default=None)
    upDate = models.DateField(null=True,blank=True)


    def __init__(self, *args, **kwargs):
        super(Todo, self).__init__(*args, **kwargs)


    def save(self, *args, **kwargs):

        if self.status == 'T' :
            self.upDate = datetime.now()
        else:
            self.upDate = None
        super(Todo, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

