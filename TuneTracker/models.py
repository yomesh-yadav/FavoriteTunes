from django.db import models

# Create your models here.
class artist(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self) :
        return self.name

class song(models.Model):
    title = models.CharField(max_length= 100)
    artists = models.ManyToManyField(artist)

    def __str__(self) :
        return self.title

