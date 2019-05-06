from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Events(models.Model):
    Event_Type = models.CharField(max_length=35)

    def __str__(self):
        return self.Event_Type


class Ethnic(models.Model):
    Language = models.CharField(max_length=35)

    def __str__(self):
        return self.Language


class Deejay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    DJ_name = models.CharField(max_length=50)
    age = models.IntegerField()
    picture = models.FileField()
    contact = models.IntegerField()
    email = models.EmailField()
    music_type = models.TextField()

    def __str__(self):
        return self.DJ_name


class Mc(models.Model):
    ethnic = models.ForeignKey(Ethnic, on_delete=models.PROTECT)
    Mc_name = models.CharField(max_length=50)
    age = models.IntegerField()
    picture = models.FileField()

    def __str__(self):
        return self.Mc_name


class CreateMc(models.Model):
    mc = models.ForeignKey(Mc, on_delete=models.CASCADE)
    Mc_name = models.CharField(max_length=20)

    def __str__(self):
        return self.Mc_name


class Planner(models.Model):
    event_type = models.ForeignKey(Events, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    picture = models.FileField()
    Age = models.IntegerField()

    def __str__(self):
        return self.name


class Hype(models.Model):
    event_type = models.ForeignKey(Events, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    picture = models.FileField()

    def __str__(self):
        return self.name


class Speakers(models.Model):
    picture = models.FileField()
    owner = models.CharField(max_length=30, blank=True)
    desc = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.owner


class CreateSpeaker(models.Model):
    speaker = models.ForeignKey(Speakers, on_delete=models.CASCADE)
    owner = models.CharField(max_length=20)

    def __str__(self):
        return self.owner






