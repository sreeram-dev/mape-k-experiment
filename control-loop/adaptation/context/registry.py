# -*-coding:utf-8 -*-
from context.dto.context import InstanceCountContext

HAPROXY_LOW_INSTANCES = 'low_instances_haproxy'
MEDIUM_NUMBER_INSTANCES = 'medium_instances_haproxy'
HAPROXY_HIGH_INSTANCES = 'high_instances_haproxy'


"""Mapping of alert with their corresponding context
"""
CONTEXT_REGISTRY = {
    HAPROXY_LOW_INSTANCES: InstanceCountContext,
    HAPROXY_HIGH_INSTANCES: InstanceCountContext
}


class ContextRegistry:

    def __init__(self):
        self.__load_context_data()

    def __load_context_data(self):
        """Loads context data from dict or map
        """
        self.data = CONTEXT_REGISTRY


    def get_context_klass_from_registry(self, alert_name):
        """Alert Name for the context
        """
        if alert_name not in self.data:
            raise KeyError("Context for the alert is not defined")

        return self.data[alert_name]
