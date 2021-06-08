from audit.models import AuditLog


class AuditLogger(object):
    """Wrapper class for the audit logger
    """

    @classmethod
    def log_message(cls, alert_name, message):
        """logs the message
            args: :alert_name
            args: :message
        """
        audit_log = AuditLog(alert_name=alert_name, message=message)
        audit_log.save()
