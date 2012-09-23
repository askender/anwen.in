# -*- coding:utf-8 -*-
import hashlib
import markdown

import tornado.escape

from utils.avatar import *
from base import BaseHandler

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
        email=self.get_argument("email",'')
        password=self.get_argument("password",'')
        user=self.get_user_byemail(email)
        if not user:
            self.write('User unfound.')
        else:
            if user['user_pass']==hashlib.md5(password).hexdigest():
                del user['user_pass'] #user.pop('user_pass')
                self.set_secure_cookie("user", tornado.escape.json_encode(user))
                self.redirect(self.get_argument("next", "/"))
            else:
                self.write('Wrong password')


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
        name=self.get_argument("name",'')
        password=self.get_argument("password",'')
        password=hashlib.md5(password).hexdigest()
        email=self.get_argument("email",'')
        domain=self.get_argument("domain",'')
        user=self.get_user_byemail(email)
        if not user:
            user_id = self.db.execute(
                "INSERT INTO users (user_email,user_name,user_pass,user_domain) VALUES (%s,%s,%s,%s)",
                email, name, password,domain)
            user=self.get_user_byid(user_id)
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
        user = self.db.get("SELECT * FROM users WHERE user_domain = %s", name)
        if not user:
            self.redirect("/404")
        user.user_say = markdown.markdown(user.user_say)
        likes = self.db.query("SELECT * FROM likes WHERE user_id = %s", user.user_id)
        likenum = len(likes)
        user['gravatar'] = get_avatar(user.user_email,100)
        self.render("userhome.html", user=user,likenum=likenum)

    def post(self):
        self.get()


class UserlikeHandler(BaseHandler):
    def get(self, name):
        user = self.get_user_bydomain(name)
        if not user:
            self.redirect("/404")            
        likes = self.db.query("SELECT * FROM likes WHERE user_id = %s", user.user_id)
        likenum = len(likes)
        for i in range(0,likenum):
            share = self.db.get("SELECT * FROM `shares` WHERE `id`=%s", likes[i]['share_id'])
            likes[i]["title"] = share.title
            likes[i]['id'] = share.id
            likes[i]['type'] = share.sharetype
        user['gravatar'] = get_avatar(user.user_email,100)
        self.render("userlike.html", user=user,likenum=likenum,likes=likes)

    def post(self):
        self.get()


class SettingHandler(BaseHandler):
    def get(self):
        if self.current_user:
            user = self.get_user_bycookie()
            if not user: self.redirect("/")
            user.gravatar = get_avatar(user.user_email,100)
            self.render("setting.html", user=user)
        else:
            self.redirect("/")

    def post(self):
        name = self.get_argument("name",'')
        city = self.get_argument("city",'')
        say = self.get_argument("say",'')
        self.db.execute(
                "UPDATE users SET user_name = %s,user_city = %s,user_say = %s "
                "WHERE user_id = %s", name,city,say,self.current_user["user_id"])
        self.redirect("/setting")


class ChangePassHandler(BaseHandler):
    def get(self):
        if self.current_user:
            user = self.get_user_bycookie()
            if not user: self.redirect("/")
            user.gravatar = get_avatar(user.user_email,100)
            self.render("changepass.html", user=user)
        else:
            self.redirect("/")

    def post(self):
        oldpass=self.get_argument("oldpass",'')
        newpass=self.get_argument("newpass",'')
        newpass=hashlib.md5(newpass).hexdigest()
        user=self.get_user_bycookie()
        if not user:
            self.write('User unfound.')
        else:
            if user['user_pass']==hashlib.md5(oldpass).hexdigest():
                self.db.execute(
                "UPDATE users SET user_pass = %s "
                "WHERE user_id = %s", newpass,self.current_user["user_id"])
                self.redirect("/setting")
            else:
                self.write('Wrong password')


class MemberHandler(BaseHandler):
    def get(self):
        members = self.db.query("SELECT `user_id`,`user_name`,`user_email` FROM `users` ORDER BY user_id "
                                "DESC LIMIT 50")
        self.render("member.html", members=members)