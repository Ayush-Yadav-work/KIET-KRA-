from rest_framework import viewsets
from .models import Department, AccreditationCriteria, KRAMetric
from .serializers import DepartmentSerializer, AccreditationCriteriaSerializer, KRAMetricSerializer
from accounts.permissions import IsSuperAdmin

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsSuperAdmin]

class AccreditationCriteriaViewSet(viewsets.ModelViewSet):
    queryset = AccreditationCriteria.objects.all()
    serializer_class = AccreditationCriteriaSerializer
    permission_classes = [IsSuperAdmin]

class KRAMetricViewSet(viewsets.ModelViewSet):
    queryset = KRAMetric.objects.all()
    serializer_class = KRAMetricSerializer
    permission_classes = [IsSuperAdmin]
