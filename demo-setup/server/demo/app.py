# -*- coding:utf-8 -*-

import falcon
import json
import logging

from demo.log_config import get_stdout_handler
from demo.log_config import get_stderr_handler
# from demo.log_config import get_syslog_handler


logger = logging.getLogger('DemoService')
logger.addHandler(get_stdout_handler())
logger.addHandler(get_stderr_handler())
# logger.addHandler(get_syslog_handler())
logger.setLevel(logging.INFO)


class ResponseLoggerMiddleware(object):
    def process_response(self, req, resp, resource, req_succeeded):
        if "haproxy" not in req.path:
            logger.info('{0} {1} {2}'.format(
                req.method, req.relative_uri, resp.status[:3]))


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

        logger.info("Ready check has been successful")

        res.body = json.dumps(payload)
        res.status = falcon.HTTP_200


class HAProxyCheck(object):

    def on_get(self, req, res):
        """Check for haproxy check
        """
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


# api.add_route("/live-check", LivelinessResource())
api = application = falcon.API(middleware=[ResponseLoggerMiddleware()])
api.add_route("/ready-check", ReadyResource())
api.add_route("/haproxy-check", HAProxyCheck())
api.add_route('/', IndexResource())
