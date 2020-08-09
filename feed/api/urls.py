from django.urls import path, include

from rest_framework.routers import DefaultRouter

from feed.api import views

router = DefaultRouter()
router.register('feed', views.FeedItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]