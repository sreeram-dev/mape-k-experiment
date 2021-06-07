from django.db import models

# Create your models here.


class AuditLog(models.Model):
    """
    """
    alert_name = models.CharField(max_length=250, required=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
