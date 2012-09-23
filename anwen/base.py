# -*- coding:utf-8 -*-

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)

    def get_user_bycookie(self):
        user=self.db.get("SELECT `user_id`,`user_name`,`user_email`,`user_domain` FROM `users` WHERE `user_id`=%s", self.current_user["user_id"])
        return user

    def get_user_byemail(self,userkey):
        user=self.db.get("SELECT `user_id`,`user_name`,`user_email`,`user_domain`,`user_pass` FROM `users` WHERE `user_email`=%s", userkey)
        return user

    def get_user_byid(self,userkey):
        user=self.db.get("SELECT `user_id`,`user_name`,`user_email`,`user_domain` FROM `users` WHERE `user_id`=%s", userkey)
        return user

    def get_user_bydomain(self,userkey):
        user=self.db.get("SELECT `user_id`,`user_name`,`user_email`,`user_domain` FROM `users` WHERE `user_domain`=%s", userkey)
        return user


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




