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

    colorChoices = (
        ('danger', 'danger'),
        ('warning', 'warning'),
        ('active', 'active'),
    )

    title = models.CharField(max_length=100)
    dateCreated = models.DateField(null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    priority = models.CharField(max_length=3, choices=priorityChoices, default='1')
    status = models.CharField(max_length=10,choices=statusChoices,default='ND')
    description = models.CharField(max_length=100,default='',null=True,blank=True)
    finishDate = models.DateField(null=True,blank=True)


    def __init__(self, *args, **kwargs):
        super(Todo, self).__init__(*args, **kwargs)


    def save(self, *args, **kwargs):

        if self.status == 'T' :
            self.finishDate = datetime.now()
        else:
            self.finishDate = None
        super(Todo, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

