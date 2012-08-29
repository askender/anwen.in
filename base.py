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

    def get_user_bycookie(self):
        user=self.db.get("SELECT * FROM `users` WHERE `user_id`=%s", self.current_user["user_id"])
        return user

    def get_user_byemail(self,userkey):
        user=self.db.get("SELECT `user_id`,`user_name`,`user_email`,`user_domain`,`user_pass` FROM `users` WHERE `user_email`=%s", userkey)
        return user

    def get_user_byid(self,userkey):
        user=self.db.get("SELECT * FROM `users` WHERE `user_id`=%s", userkey)
        return user

    def get_user_bydomain(self,userkey):
        user=self.db.get("SELECT * FROM `users` WHERE `user_domain`=%s", userkey)
        return user

    def get_avatar(self, email, size):
        gravatar_id = hashlib.md5(email.lower()).hexdigest()
        size = str(size)
        return "http://www.gravatar.com/avatar/%s?size=%s" % (gravatar_id,size)