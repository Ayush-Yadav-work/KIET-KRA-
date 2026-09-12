from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, AccreditationCriteriaViewSet, KRAMetricViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'accreditation-criteria', AccreditationCriteriaViewSet)
router.register(r'kra-metrics', KRAMetricViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
