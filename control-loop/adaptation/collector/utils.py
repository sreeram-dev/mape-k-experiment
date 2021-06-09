# -*- coding: utf-8 -*-

from typing import Dict

from audit.logger import AuditLogger
from context.registry import ContextRegistry
from goals.rules.manager import RulesManager


class AdaptationManager:
    context_registry = ContextRegistry()
    rules_manager = RulesManager()

    @classmethod
    def process_alert(cls, alert: Dict):
        """Process an alert
        """
        fingerprint = alert['fingerprint']
        job_source = alert['labels']['job']
        alert_name = alert['labels']['alertname']
        alert_job = f"{alert_name}_{job_source}"
        context_klass = cls.context_registry.get_context_klass_from_registry(alert_job)
        context = context_klass(alert)
        message = f"Received {alert_job} with value: {alert['labels']['alertvalue']} and identified context: {context.get_name()}"
        AuditLogger.log_message(message, fingerprint=fingerprint)
        best_rule = cls.rules_manager.get_action_for_context(context)
        message = f"Identified rule for alert: {alert_job} || {best_rule.get_name()}"
        AuditLogger.log_message(message, fingerprint=fingerprint)
        best_rule.perform_action(alert_job)
        message = f"Adaptation for alert: {alert_job} and rule: {best_rule.get_name()}"
        AuditLogger.log_message(message, fingerprint=fingerprint)
