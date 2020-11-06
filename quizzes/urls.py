from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('quiz', QuizzesViewSet)
router.register('era', ErasViewSet)
router.register('level', LevelsViewSet)

urlpatterns = router.urls