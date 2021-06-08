# -*- coding:utf-8 -*-


class AlertManagerContext:

    def __init__(self, alert):
        self.__populate_common_fields(alert)

    def __populate_common_fields(self, alert):
        self.fingerprint = alert['fingerprint']
        self.start_time = alert['startsAt']
        self.end_time = alert['endsAt']
        job_source = alert['labels']['job']
        self.source_ip = alert['labels']['instance']
        alert_name = alert['labels']['alertname']
        self.alert_job = f"{alert_name}_{job_source}"
        self.alert_value = alert['labels']['alertvalue']

    def get_fingerprint(self):
        """Get the unique fingerprint of the alert
        """
        return self.fingerprint

    def get_source(self):
        """Get the source of the alert
        """
        return {
            'source_ip': self.source_ip,
            'alert_job_pair': self.alert_job
        }

    def get_name(self):
        """Get the name of the alert
        """
        raise NotImplementedError

    def get_alert_job(self):
        """Source of the context in alertmanager
        """
        raise NotImplementedError

    def get_value(self):
        """Get the value of the alert
        """
        return self.alert_value

    def get_children(self):
        """Get the atomic or dynamic contexts that make up the app
        """
        raise NotImplementedError


class InstanceCountContext(AlertManagerContext):

    def __init__(self, alert):
        super(InstanceCountContext, self).__init__(alert)
        self.name = "InstanceCount"
        self.is_atomic = True
        self.alert_value = int(self.alert_value)

    def get_name(self):
        return self.name

    def get_alert_job(self):
        return self.alert_job

    def is_atomic_context(self) -> bool:
        return self.is_atomic

    def get_children(self):
        """If not, Atomic Context,
        """
        if self.is_atomic:
            return []
        return []
