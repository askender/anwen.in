# -*- coding:utf-8 -*-

from tornado.escape import json_decode
from tornado.web import RequestHandler, HTTPError
import json
from log import logger


class BaseHandler(RequestHandler):

    def get_user_lang(self):
        return self.request.headers['Accept-Language']

    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if not user_json:
            return None
        return json_decode(user_json)


def require_login(method):
    """Decorate methods with this to require user logged in."""
    import functools

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            raise HTTPError(403)
        return method(self, *args, **kwargs)
    return wrapper


class JSONHandler(BaseHandler):
    """Every API handler should inherit from this class."""

    def post_prepare(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header(
            'Access-Control-Allow-Headers',
            'X-Requested-With, Origin, Authorization, Content-Type, Accept'
        )

    def options(self, *args, **kwargs):
        pass

    def get_json_arg(self, name=None, *args):
        """Returns the value of the argument with the given name,
        from JSON-formated body"""

        headers = self.request.headers
        if not ('Content-Type' in headers
                and 'application/json' in headers['Content-Type']):
            logger.warn('Content-Type is not JSON, ignored.')
        try:
            obj = json.loads(self.request.body)
        except ValueError:
            raise HTTPError(400,
                            'Request body is not JSON formatted!'
                            )

        if not name:
            return obj
        try:
            return obj[name]
        except KeyError:
            if len(args) > 0:
                return args[0]
            else:
                raise HTTPError(400,
                                'Missing argument [%s]!' % name
                                )

    def write_json(self, obj):
        """Writes the JSON-formated string of the give obj
        to the output buffer"""

        self.set_header('Content-Type', 'application/json')
        from json import dumps

        def handler(obj):
            print repr(obj)
            return dict(obj)
        s = dumps(obj)  # default=handler
        return self.write(s)

    # def get_user_locale(self):
    #     if "locale" not in self.current_user.prefs:
    #         # Use the Accept-Language header
    #         return None
    #     return self.current_user.prefs["locale"]
