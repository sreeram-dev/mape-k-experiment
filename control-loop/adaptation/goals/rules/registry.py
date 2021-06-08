# -*- coding: utf-8 -*-
from goals.rules.ratelimits import IncreaseRateLimit, DecreaseRateLimit

RULES_REGISTRY = [
    (0.75, IncreaseRateLimit()),
    (0.65, DecreaseRateLimit()),
]
