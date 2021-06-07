# -*- coding:utf-8 -*-

from audit.models import AuditLog


class AuditLogger(object):
    """
    """


    @classmethod
    def log_message(cls, alert_name, message):
        """
        """
        audit_log = AuditLog(alert_name=alert_name, message=message)
        audit_log.save()
