# -*- coding:utf-8 -*-

import os.path
import tornado.database
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# import code for encoding urls and generating md5 hashes
import urllib, hashlib

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)

    def get_userinfo(self):
        if self.current_user:
            user=self.db.get("SELECT `user_id`,`user_name`,`user_email`,`user_domain` FROM `users` WHERE `user_email`=%s", email)
        return user