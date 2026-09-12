from rest_framework import serializers
from .models import Department, AccreditationCriteria, KRAMetric

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class AccreditationCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccreditationCriteria
        fields = '__all__'

class KRAMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = KRAMetric
        fields = '__all__'
