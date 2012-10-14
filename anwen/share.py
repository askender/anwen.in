# -*- coding:utf-8 -*-

import markdown
import urllib2
import datetime
import tornado.web
from utils.avatar import *
from base import BaseHandler
from peewee import F
from models import User, Share, Comment, Like

class ShareHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = self.get_argument("id", None)
        share = None
        if id:
            share = Share.get(id = id)
        self.render("share.html", share = share)

    @tornado.web.authenticated
    def post(self):
        id = self.get_argument("id", None)
        title = self.get_argument("title")
        tag = self.get_argument("tag",None)
        markdown = self.get_argument("markdown")
        sharetype = self.get_argument("type")
        if id:
            try:
                share = Share.get(id = id)
            except:
                self.redirect("/404")
            share = Share.update(title = title,
                                markdown = markdown,
                                sharetype = sharetype,
                                updated = datetime.datetime.now()
                            ).where(id = id).execute()
        else:
            share = Share.create(title = title,
                                markdown = markdown,
                                sharetype = sharetype,
                                user_id = self.current_user["user_id"],
                )
            user = User.update(user_leaf = F('user_leaf') +10).where(id = self.current_user["user_id"]).execute()
            id = str(share.id)
        self.redirect("/share/" + str(id))


class EntryHandler(BaseHandler):
    def get(self, id):
        try:
            share = Share.get(id = id)
            share.markdown = markdown.markdown(share.markdown)
            if self.current_user:
                share.is_liking = Like.select().where(share_id=share.id,user_id=self.current_user["user_id"]).count()>0
        except:
            self.redirect("/404")
        comments = Comment.select().where(share_id=share.id)
        for comment in comments:
            user = User.get(id = comment.user_id)
            comment.name = user.user_name
            comment.domain = user.user_domain
            comment.gravatar = get_avatar(user.user_email,50)
        hit = Share.update(hitnum = F('hitnum') +1).where(id = id).execute()
        self.render("sharee.html", share=share,comments=comments)


class CommentHandler(BaseHandler):
    def post(self):
        commentbody = self.get_argument("commentbody",None)
        share_id = self.get_argument("share_id",None)
        html = markdown.markdown(commentbody)
        comment_id = Comment.create(user_id = self.current_user["user_id"],
                                    share_id = share_id,
                                    commentbody = commentbody
                                    )
        comment = Share.update(commentnum = F('commentnum') +1).where(id = share_id).execute()
        name = tornado.escape.xhtml_escape(self.current_user["user_name"])
        email = tornado.escape.xhtml_escape(self.current_user["user_email"])
        domain = tornado.escape.xhtml_escape(self.current_user["user_domain"])
        gravatar = get_avatar(self.current_user["user_email"],50)
        newcomment = ''
        newcomment += ' <div class="comment">'
        newcomment += '<div class="avatar">'
        newcomment += '<img src="'+gravatar+'" />'
        newcomment += '</div>'
        newcomment += '<div class="name">'+name+'</div>'
        newcomment += '<div class="date" title="at"></div>'
        newcomment += html
        newcomment += '</div>'
        self.write(newcomment)

class LikeHandler(BaseHandler):
    def post(self):
        share_id = self.get_argument("share_id",None)
        likenum = self.get_argument("likenum",0)
        like_id = Like.create(user_id = self.current_user["user_id"],
                            share_id = share_id
                            )
        share = Share.get(id = share_id)
        like_share = Share.update(likenum = F('likenum')+1).where(id = share_id).execute()
        user_leaf = User.update(user_leaf = F('user_leaf')+4).where(id = share.user).execute()
        user_leaf = User.update(user_leaf = F('user_leaf')+2).where(id = self.current_user["user_id"]).execute()
        likenum = int(likenum) + 1
        newlikes = ':) ' + str(likenum)
        self.write(newlikes)


class FeedHandler(BaseHandler):
    def get(self):
        shares = Share.select()
        self.set_header("Content-Type", "application/atom+xml")
        self.render("feed.xml", shares=shares)