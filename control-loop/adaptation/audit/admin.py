import datetime

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from audit.models import AuditLog


class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('alert_fingerprint', 'message', 'created_at_milli')
    list_filter = ('alert_fingerprint', )
    ordering = ['-created_at']
    search_fields = ('alert_fingerprint', )
    list_per_page = 30

    @admin.display(description='created_at')
    def created_at_milli(self, obj: AuditLog):
        str_time = obj.created_at.strftime("%d %b %Y %H:%M:%S:%f")
        return str_time

admin.site.register(AuditLog, AuditLogAdmin)
