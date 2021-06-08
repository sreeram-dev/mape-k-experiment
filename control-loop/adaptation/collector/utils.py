# -*- coding: utf-8 -*-

from typing import Dict

from context.registry import ContextRegistry
from goals.rules.manager import RulesManager


class AdaptationManager:
    context_registry = ContextRegistry()
    rules_manager = RulesManager()

    @classmethod
    def process_alert(cls, alert: Dict):
        """Process an alert
        """
        job_source = alert['labels']['job']
        alert_name = alert['labels']['alertname']
        alert_job = f"{alert_name}_{job_source}"
        context_klass = cls.context_registry.get_context_klass_from_registry(alert_job)
        context = context_klass(alert)
        best_rule = cls.rules_manager.get_action_for_context(context)
        best_rule.perform_action()

