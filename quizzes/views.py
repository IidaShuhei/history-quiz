from rest_framework.viewsets import ModelViewSet
from .models import Quiz
from .serializers import *
from django_filters import rest_framework as filters

class QuizzesViewSet(ModelViewSet):
  order = ('era_id','category_id','order')
  queryset = Quiz.objects.all().order_by(*order)
  serializer_class = QuizSerializer

class ErasViewSet(ModelViewSet):
  queryset = Era.objects.all().order_by('order')
  serializer_class = EraSerializer

class LevelsViewSet(ModelViewSet):
  sql = "select * from levels"
  queryset = Level.objects.raw(sql)
  serializer_class = LevelSerializer

class CategoriesViewSet(ModelViewSet):
  order = ('era_id','order')
  queryset = Category.objects.all().order_by(*order)
  serializer_class = CategorySerializer