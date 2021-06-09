# -*- coding: utf-8 -*-

from typing import Dict

import rule_engine

from context.registry import HAPROXY_OPTIMAL_INSTANCES, HAPROXY_LOW_INSTANCES
from context.registry import  HAPROXY_HIGH_INSTANCES
from goals.providers.haproxy import HAProxyProvider
from goals.rules.base import BaseRule


class DecreaseRateLimit(BaseRule):
    action_provider = HAProxyProvider()
    name = 'DecreaseRateLimit'

    def __init__(self):
        self.context = rule_engine.Context(type_resolver=rule_engine.type_resolver_from_dict({
            'context_name': rule_engine.DataType.STRING,
        }))
        self.rule_str = 'context_name == "low_instances_haproxy"'
        self.rule = rule_engine.Rule(self.rule_str, context=self.context)

    def get_rule(self):
        return self.rule

    def is_rule_triggered(self, params: Dict):
        print(params)
        return self.rule.matches(params)

    def perform_action(self, payload={}):
        self.action_provider.replace_entry_to_map("ratelimit.map", "rate_limit", 500)

    def get_context(self):
        return self.context


class IncreaseRateLimit(BaseRule):
    action_provider = HAProxyProvider()
    name = 'IncreaseRateLimit'

    def __init__(self):
        self.context = rule_engine.Context(type_resolver=rule_engine.type_resolver_from_dict({
            'context_name': rule_engine.DataType.STRING,
        }))
        self.rule_str = 'context_name == "high_instances_haproxy"'
        self.rule = rule_engine.Rule(self.rule_str, context=self.context)

    def get_rule(self):
        return self.rule

    def is_rule_triggered(self, params: Dict):
        return self.rule.matches(params)

    def perform_action(self, alert_job, payload={}):
        self.action_provider.replace_entry_to_map("ratelimit.map", "rate_limit", 2000)

    def get_context(self):
        return self.context


class AdjustRateLimit(BaseRule):
    action_provider = HAProxyProvider()
    name = 'AdjustRateLimit'

    def __init__(self):
        self.context = rule_engine.Context(type_resolver=rule_engine.type_resolver_from_dict({
            'context_name': rule_engine.DataType.STRING,
        }))
        self.rule_str = 'context_name == "optimal_instances_haproxy"'
        self.rule = rule_engine.Rule(self.rule_str, context=self.context)

    def get_rule(self):
        return self.rule

    def is_rule_triggered(self, params: Dict):
        return self.rule.matches(params)

    def perform_action(self, alert_job, payload={}):
        self.action_provider.replace_entry_to_map("ratelimit.map", "rate_limit", 1000)

    def get_context(self):
        return self.context
