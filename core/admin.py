from django.contrib import admin
from .models import Department, AccreditationCriteria, KRAMetric

admin.site.register(Department)
admin.site.register(AccreditationCriteria)
admin.site.register(KRAMetric)
