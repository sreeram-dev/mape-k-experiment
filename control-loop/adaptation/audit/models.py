from django.db import models

# Create your models here.


class AuditLog(models.Model):
    alert_fingerprint = models.CharField(max_length=150, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
