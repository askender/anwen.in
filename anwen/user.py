# -*- coding:utf-8 -*-

import hashlib
import markdown

import tornado.escape

from utils.avatar import *
from base import BaseHandler
from models import User, Share, Like

class LoginHandler(BaseHandler):
    def get(self):
        if self.current_user:
            self.redirect("/")
            return
        self.set_cookie("checkflag", "true")
        self.render("login.html")

    def post(self):
        if not self.request.headers.get("Cookie"):  
            self.render("require_enable_cookie.html")  
            return
        email = self.get_argument("email",'')
        password = self.get_argument("password",'')
        try:
            u = User.get(
                user_email=email,
                user_pass=hashlib.md5(password).hexdigest()
            )
        except User.DoesNotExist:
            self.write('密码错误或用户不存在，请重新注册或登录')
        else:
            user = {'user_id':u.id,
                    'user_name':u.user_name,
                    'user_email':u.user_email,
                    'user_domain':u.user_domain}
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
            self.redirect(self.get_argument("next", "/"))


class JoinusHandler(BaseHandler):
    def get(self):
        if self.current_user:  
            self.redirect("/")  
            return
        self.set_cookie("checkflag", "true")
        self.render("joinus.html")
    def post(self):
        if not self.request.headers.get("Cookie"):  
            self.render("require_enable_cookie.html")  
            return
        name = self.get_argument("name",'')
        password = self.get_argument("password",'')
        password = hashlib.md5(password).hexdigest()
        email = self.get_argument("email",'')
        domain = self.get_argument("domain",'')
        try:
            user = User.get(user_email = email)
        except:
            u = User.create(user_name = name,
                            user_pass = password,
                            user_email = email,
                            user_domain = domain,
                )
            user = {'user_id':u.id,
                    'user_name':u.user_name,
                    'user_email':u.user_email,
                    'user_domain':u.user_domain}
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
            self.redirect(self.get_argument("next", "/"))
        else:
            self.write('用户已经存在，请重新注册或直接登录')


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect(self.get_argument("next", "/"))

    def post(self):
        self.get()


class UserhomeHandler(BaseHandler):
    def get(self, name):
        try:
            user = User.get(user_domain = name)
        except:
            self.redirect("/404")
        user.user_say = markdown.markdown(user.user_say)
        likenum = Like.select().where(user_id=user.id).count()
        user.gravatar = get_avatar(user.user_email,100)
        self.render("userhome.html", user = user,likenum = likenum)

    def post(self):
        self.get()


class UserlikeHandler(BaseHandler):
    def get(self, name):
        try:
            user = User.get(user_domain=name)
        except:
            self.redirect("/404")          
        likes = Like.select().where(user_id=user.id)
        likenum = likes.count()
        for like in likes:
            share = Share.get(id=like.share_id)
            like.title = share.title
            like.id = share.id
            likes.type = share.sharetype
        user.gravatar = get_avatar(user.user_email,100)
        self.render("userlike.html", user = user,likenum = likenum,likes = likes)

    def post(self):
        self.get()


class SettingHandler(BaseHandler):
    def get(self):
        if self.current_user:
            user = User.get(id=self.current_user["user_id"])
            if not user:
                self.redirect("/")
            user.gravatar = get_avatar(user.user_email,100)
            self.render("setting.html", user = user)
        else:
            self.redirect("/")

    def post(self):
        name = self.get_argument("name",None)
        city = self.get_argument("city",None)
        say = self.get_argument("say",None)
        user = User.update(user_name=name,
                    user_city=city,
                    user_say=say
                    ).where(id=self.current_user["user_id"]).execute()
        self.redirect("/setting")


class ChangePassHandler(BaseHandler):
    def get(self):
        if self.current_user:
            user = User.get(id=self.current_user["user_id"])
            if not user:
                self.redirect("/")
            user.gravatar = get_avatar(user.user_email,100)
            self.render("changepass.html", user = user)
        else:
            self.redirect("/")

    def post(self):
        oldpass = self.get_argument("oldpass",'')
        newpass = self.get_argument("newpass",'')
        newpass = hashlib.md5(newpass).hexdigest()
        user = self.get_user_bycookie()
        if not user:
            self.write('User unfound.')
        else:
            if user.user_pass == hashlib.md5(oldpass).hexdigest():
                User.update(user_pass = newpass).where(id=elf.current_user["user_id"]).execute()
                self.redirect("/setting")
            else:
                self.write('Wrong password')


class MemberHandler(BaseHandler):
    def get(self):
        members = User.select()
        self.render("member.html", members = members)