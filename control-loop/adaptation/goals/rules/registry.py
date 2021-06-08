# -*- coding: utf-8 -*-
from goals.rules.ratelimits import IncreaseRateLimit, DecreaseRateLimit, AdjustRateLimit

RULES_REGISTRY = [
    (0.75, IncreaseRateLimit()),
    (0.65, DecreaseRateLimit()),
    (0.50, AdjustRateLimit())
]
