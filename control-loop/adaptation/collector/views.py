import json

from django.http import JsonResponse
from django.views import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpRequest

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
        """
        """
        print(json.loads(request.body))
        return JsonResponse({
            'message': 'request acknowledged and adaptation triggered',
            'success': True
        })
