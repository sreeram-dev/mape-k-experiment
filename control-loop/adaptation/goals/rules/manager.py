import heapq

from context.dto.context import AlertManagerContext

from goals.rules.registry import RULES_REGISTRY

class RulesManager:

    def get_action_for_context(self, context: AlertManagerContext):
        """Get Action from Context
        """
        params = {
            'context_name': context.get_alert_job()
        }

        applicable_rules = []
        for weight, rule in RULES_REGISTRY:
            if rule.is_rule_triggered(params):
                applicable_rules.append((weight, rule))

        best_possible_rule = heapq.nlargest(1, applicable_rules)
        return best_possible_rule[0][1]
