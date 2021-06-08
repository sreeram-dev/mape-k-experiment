import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpRequest

from audit.logger import AuditLogger
from collector.utils import AdaptationManager


@method_decorator(csrf_exempt, name='dispatch')
class AlertCollectionView(View):
    http_method_names = ['get', 'post', 'put']

    def get(self, request, *args, **kwargs):
        """
        """
        return JsonResponse({
            'message': 'request acknowledged',
            'success': True
        })

    def post(self, request: HttpRequest, *args, **kwargs):
        """Sample Payload {
            'receiver': 'adaptation-framework',
            'status': 'firing',
            'alerts': [{'status': 'firing', 'labels': {'alertname': 'Low number of instances', 'alias': 'haproxy',
                            'instance': '192.168.0.33:8404', 'job': 'haproxy', 'proxy': 'webservers', 'severity': 'critical'},
                        'annotations': {'description': 'Low number of webservers detected, please adjust ratelimits', 'summary': 'Low number of backend instances'},
                        'startsAt': '2021-06-08T02:18:16.673029836Z',
                        'endsAt': '0001-01-01T00:00:00Z',
                        'generatorURL': 'http://localhost:9090/graph?g0.expr=haproxy_backend_active_servers%7Bproxy%3D%22webservers%22%7D+%3D%3D+1&g0.tab=1',
                        'fingerprint': '57faf96f7fdfea9d'}],
            'groupLabels': {'alertname': 'Low number of instances'},
            'commonLabels': {'alertname': 'Low number of instances', 'alias': 'haproxy', 'instance': '192.168.0.33:8404', 'job': 'haproxy', 'proxy': 'webservers', 'severity': 'critical'},
            'commonAnnotations': {'description': 'Low number of webservers detected, please adjust ratelimits', 'summary': 'Low number of backend instances'},
            'externalURL': 'http://localhost:9093',
            'version': '4',
            'groupKey': '{}:{alertname="Low number of instances"}',
            'truncatedAlerts': 0
        }
        """


        payload = json.loads(request.body)
        for alert in payload['alerts']:
            AdaptationManager.process_alert(alert)

        return JsonResponse({
            'message': 'request acknowledged and adaptation triggered',
            'success': True
        })
