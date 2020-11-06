from rest_framework.serializers import ModelSerializer
from .models import *

class QuizSerializer(ModelSerializer):
  class Meta:
    model = Quiz
    fields = '__all__'

class EraSerializer(ModelSerializer):
  class Meta:
    model = Era
    fields = '__all__'

class LevelSerializer(ModelSerializer):
  class Meta:
    model = Level
    fields = '__all__'