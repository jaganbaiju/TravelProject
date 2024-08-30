from django.db import models

# Create your models here.


class PlaceModel(models.Model):
    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='PlaceImg')
    desc = models.TextField()

    def __str__(self):
        return self.name


class TeamModel(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='TeamImg')
    desc = models.TextField()

    def __str__(self):
        return self.name
