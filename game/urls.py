from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, PlayerViewSet, GameViewSet, ScoreViewSet, UserViewSet, GroupViewSet, UserActivityViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'team', TeamViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'game', GameViewSet)
router.register(r'score', ScoreViewSet)
router.register(r'user_activity', UserActivityViewSet)

urlpatterns = [
    path('', include(router.urls))
]