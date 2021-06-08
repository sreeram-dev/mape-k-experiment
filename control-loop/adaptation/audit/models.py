from django.db import models

# Create your models here.


class AuditLog(models.Model):
    alert_name = models.CharField(max_length=250)
    alert_fingerprint = models.CharField(max_length=150)
    alert_summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
