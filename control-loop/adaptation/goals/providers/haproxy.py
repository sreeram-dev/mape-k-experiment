# -*- coding: utf-8 -*-

import os
import json

import requests
from requests import RequestException

from requests.auth import HTTPBasicAuth


class HAProxyProvider:
    """Provider for HAPROXY DataPlane API
    """
    HOST = 'http://haproxy:9999/v2'
    USERNAME = os.environ.get('DATAPLANE_API_USERNAME')
    PASSWORD = os.environ.get('DATAPLANE_API_PASSWORD')

    def replace_entry_to_map(self, map_file: str, key: str, value):
        """Adds an entry to map file
        """
        key_id = 'rate_limit'
        full_url = f"{self.HOST}/services/haproxy/runtime/maps_entries/{key_id}"
        auth = HTTPBasicAuth(self.USERNAME, self.PASSWORD)
        data = json.dumps({"value": str(value)})
        params = {
            'map': map_file,
            'force_sync': "true"
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.put(full_url, auth=auth, data=data,
                                 params=params, headers=headers)
        # raise httperror
        response.raise_for_status()

        return response



