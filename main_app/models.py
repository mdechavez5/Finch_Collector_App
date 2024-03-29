from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dancer(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Choreo(models.Model):
    title = models.CharField(max_length=150)
    vid = models.CharField(max_length=250)
    embed = models.CharField(max_length=300)
    dancer = models.ForeignKey(Dancer, on_delete=models.CASCADE, related_name="choreo")

    def __str__(self):
        return self.title

class Team(models.Model):
    title = models.CharField(max_length=150)
    img = models.CharField(max_length=250, default=1)
    # this is going to create the many to many relationship and join table
    dancers = models.ManyToManyField(Dancer)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    choreos = models.ManyToManyField(Choreo)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


