from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('model', views.CancerModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
]