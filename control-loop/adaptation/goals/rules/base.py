# -*- coding:utf-8 -*-


class BaseRule:
    name = 'BaseRule'

    def get_rule(self):
        raise NotImplementedError

    def is_rule_triggered(self):
        raise NotImplementedError

    def perform_action(self):
        raise NotImplementedError

    def get_context(self):
        raise NotImplementedError

    def get_name(self):
        return self.name
