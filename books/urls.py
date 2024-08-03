from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RecommendationViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'recommendations', RecommendationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
