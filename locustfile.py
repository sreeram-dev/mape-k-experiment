# -*- coding:utf-8 -*-

import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(2)
    def home_page(self):
        self.client.get("/")

    @task(3)
    def ready_check(self):
        self.client.get("/ready-check")
