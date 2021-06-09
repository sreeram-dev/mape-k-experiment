from audit.models import AuditLog


class AuditLogger(object):
    """Wrapper class for the audit logger
    """

    @classmethod
    def log_message(cls, message, fingerprint=None):
        """logs the message
            args: :alert_name
            args: :message
        """
        if fingerprint:
            audit_log = AuditLog(alert_fingerprint=fingerprint, message=message)
        else:
            audit_log = AuditLog(message=message)

        audit_log.save()
