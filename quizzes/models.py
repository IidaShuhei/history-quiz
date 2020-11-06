from django.db import models

# Create your models here.
class Era(models.Model):
  era = models.CharField(max_length=255)
  def __str__(self):
    return self.era

class Level(models.Model):
  level = models.CharField(max_length=100)
  def __str__(self):
    return self.level

class Quiz(models.Model):
  question = models.TextField(max_length=500)
  answer =  models.CharField(max_length=300)
  era_id = models.ForeignKey(Era, on_delete=models.CASCADE)
  level_id = models.ForeignKey(Level, on_delete=models.CASCADE)
  status = models.IntegerField()
  def __str__(self):
    return self.question