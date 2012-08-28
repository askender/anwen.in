# -*- coding:utf-8 -*-
#music envelope heart user film time road download-alt flag headphones book bookmark camera picture pencil question-sign gift leaf fire eye-open comment magnet retweet hdd bullhorn bell thumbs-up thumbs-down globe tasks
#pencil music film user road book picture  fire eye-open question-sign
import tornado.database
import tornado.web

from base import *
from settings import *

import markdown
import re
import unicodedata
import urllib2


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = self.get_argument("id", None)
        share = None
        if id:
            share = self.db.get("SELECT * FROM shares WHERE id = %s", int(id))
        self.render("share.html", share=share)

    @tornado.web.authenticated
    def post(self):
        id = self.get_argument("id", None)
        title = self.get_argument("title")
        tag = self.get_argument("tag",None)
        text = self.get_argument("markdown")
        sharetype = self.get_argument("type")
        html = markdown.markdown(text)
        if id:
            share = self.db.get("SELECT * FROM shares WHERE id = %s", int(id))
            if not share: raise tornado.web.HTTPError(404)
            self.db.execute(
                "UPDATE shares SET title = %s, markdown = %s, html = %s,"
                "sharetype = %s"
                "WHERE id = %s", title, text, html,sharetype,int(id))
        else:
            share_id = self.db.execute(
                "INSERT INTO shares (author_id,title,markdown,html,sharetype,"
                "published) VALUES (%s,%s,%s,%s,%s,UTC_TIMESTAMP())",
                self.current_user["user_id"], title, text, html,sharetype)
            self.db.execute(
                "UPDATE users SET user_leaf = user_leaf+10 "
                "WHERE user_id = %s", self.current_user["user_id"])
            id = str(share_id)
        self.redirect("/share/" + str(id))


class EntryHandler(BaseHandler):
    def get(self, id):
        share = self.db.get("SELECT * FROM shares WHERE id = %s", id)
        if not share: raise tornado.web.HTTPError(404)
        comments = self.db.query("SELECT * FROM comments WHERE share_id = %s ORDER BY id DESC", id)
        commentnum = len(comments)
        for i in range(0,commentnum):
            user = get_user_byid(comments[i]['author_id'])
            comments[i]["name"] = user.user_name
            comments[i]['domain'] = user.user_domain
            comments[i]['gravatar'] = self.get_avatar(user.user_email,50)
        self.render("sharee.html", share=share,comments=comments)


class CommentHandler(BaseHandler):
    def post(self):
        uri = self.request.body
        mydict = {}
        for i in uri.split('&'):
            data = i.split('=')
            mydict[data[0]]=data[1]
        html = urllib2.unquote(str(mydict['commentbody'])).decode("utf-8")
        html = markdown.markdown(html)
        comment_id = self.db.execute(
                "INSERT INTO comments (author_id,share_id,commentbody,"
                "commenttime) VALUES (%s,%s,%s,UTC_TIMESTAMP())",
                self.current_user["user_id"], mydict['share_id'], html)
        name = tornado.escape.xhtml_escape(self.current_user["user_name"])
        email = tornado.escape.xhtml_escape(self.current_user["user_email"])
        domain = tornado.escape.xhtml_escape(self.current_user["user_domain"])
        gravatar = self.get_avatar(user.user_email,50)
        newcomment = ''
        newcomment += ' <div class="comment">'
        newcomment += '<div class="avatar">'
        newcomment += '<img src="'+gravatar+'" />'
        newcomment += '</div>'
        newcomment += '<div class="name">'+name+'</div>'
        newcomment += '<div class="date" title="at"></div>'
        newcomment += html
        #newcomment += '<p>'+mydict['commentbody']+'</p>'
        newcomment += '</div>'
        self.write(newcomment)

class LikeHandler(BaseHandler):
    def post(self):
        uri = self.request.body
        mydict = {}
        for i in uri.split('&'):
            data = i.split('=')
            mydict[data[0]]=data[1]
        like_id = self.db.execute(
                "INSERT INTO likes (user_id,share_id,"
                "liketime) VALUES (%s,%s,UTC_TIMESTAMP())",
                self.current_user["user_id"], mydict['share_id'])
        like_share = self.db.execute(
                "UPDATE shares SET likes = likes+1 "
                "WHERE id = %s", mydict['share_id'])
        self.db.execute(
                "UPDATE users SET user_leaf = user_leaf+1 "
                "WHERE user_id = %s", self.current_user["user_id"])
        self.db.execute(
                "UPDATE users SET user_leaf = user_leaf+2 "
                "WHERE user_id = %s", self.current_user["user_id"])
        likenum = int(mydict['share_likes']) + 1
        #name = tornado.escape.xhtml_escape(self.current_user["user_name"])
        newlikes = ':) ' + str(likenum)
        self.write(newlikes)


class FeedHandler(BaseHandler):
    def get(self):
        shares = self.db.query("SELECT * FROM shares ORDER BY published "
                                "DESC LIMIT 10")
        self.set_header("Content-Type", "application/atom+xml")
        self.render("feed.xml", shares=shares)