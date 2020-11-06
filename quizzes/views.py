from rest_framework.viewsets import ModelViewSet
from .models import Quiz
from .serializers import *
from django_filters import rest_framework as filters

class QuizzesViewSet(ModelViewSet):
  queryset = Quiz.objects.all().order_by('id')
  serializer_class = QuizSerializer

class ErasViewSet(ModelViewSet):
  queryset = Era.objects.all()
  serializer_class = EraSerializer

class LevelsViewSet(ModelViewSet):
  sql = "select * from quizzes_level"
  queryset = Level.objects.raw(sql)
  serializer_class = LevelSerializer