# -*- coding:utf-8 -*-

import tornado.web
from models import Ande

class BaseHandler(tornado.web.RequestHandler):
    # @property #old way
    # def db(self):
    #     return self.application.db

    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)


def require_login(method):
    """Decorate methods with this to require user logged in."""
    import functools
    import tornado

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            raise tornado.web.HTTPError(403)
        return method(self, *args, **kwargs)
    return wrapper




