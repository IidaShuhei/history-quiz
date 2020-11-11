from django.db import models

# Create your models here.
class Era(models.Model):
  era = models.CharField(max_length=255,db_column='era')
  order = models.IntegerField(db_column='order')
  def __str__(self):
    return self.era
  class Meta:
    db_table = 'eras'

class Level(models.Model):
  level = models.CharField(max_length=100,db_column='level')
  def __str__(self):
    return self.level
  class Meta:
    db_table = 'levels'

class Category(models.Model):
  era_id = models.ForeignKey(Era,on_delete=models.PROTECT,db_column='era_id')
  category_name = models.CharField(max_length=255,db_column='category_name')
  order = models.IntegerField(db_column='order')
  def __str__(self):
    return self.category_name
  class Meta:
    db_table = 'categories'

class Quiz(models.Model):
  question = models.TextField(max_length=500,db_column='question')
  answer =  models.CharField(max_length=300,db_column='answer')
  era_id = models.ForeignKey(Era, on_delete=models.PROTECT,db_column='era_id')
  level_id = models.ForeignKey(Level, on_delete=models.PROTECT,db_column='level_id')
  category_id = models.ForeignKey(Category,on_delete=models.PROTECT,db_column='category_id')
  order = models.IntegerField(db_column='order')
  status = models.IntegerField(db_column='status')
  def __str__(self):
    return self.question
  class Meta:
    db_table = 'quizzes'