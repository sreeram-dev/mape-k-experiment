# -*- coding:utf-8 -*-

import falcon
import json


api = application = falcon.API()


class LivelinessResource(object):

    def on_get(self, req, res):
        """Check for liveliness
        """
        payload = {
            'success': True,
            'message': 'Image is live'
        }

        res.body = json.dumps(payload)
        res.status = falcon.HTTP_200


class ReadyResource(object):

    def on_get(self, req, res):
        """Check for liveliness
        """
        payload = {
            'success': True,
            'message': 'Ready to accept requests'
        }

        res.body = json.dumps(payload)
        res.status = falcon.HTTP_200


class IndexResource(object):

    def on_get(self, req, res):
        """Hello World resource
        """
        payload = {
            'success': True,
            'message': 'Welcome to demo server API'
        }

        res.body = json.dumps(payload)
        res.status = falcon.HTTP_200


#api.add_route("/live-check", LivelinessResource())
api.add_route("/ready-check", ReadyResource())
api.add_route('/', IndexResource())
