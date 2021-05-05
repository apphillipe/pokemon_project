from django.db import models

# Create your models here.
class Ability(models.Model):
    name = models.CharField(max_length=50)
    pokemon = models.ForeignKey()

class Pokemon(models.Model):
    
    name = models.CharField(max_length=30)
