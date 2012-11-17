# -*- coding:utf-8 -*-

import markdown
import datetime
from random import randint
import tornado.web
from utils.avatar import get_avatar
from base import BaseHandler
from peewee import F
from db.models import User, Share, Comment, Like, Hit


class ShareHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = self.get_argument("id", None)
        share = None
        if id:
            share = Share.get(id=id)
        self.render("share.html", share=share)

    @tornado.web.authenticated
    def post(self):
        id = self.get_argument("id", None)
        title = self.get_argument("title")
        markdowna = self.get_argument("markdown")
        sharetype = self.get_argument("type")
        if id:
            try:
                share = Share.get(id=id)
            except:
                self.redirect("/404")
            share = Share.update(
                title=title, markdown=markdowna,
                sharetype=sharetype,
                updated=datetime.datetime.now()).where(id=id).execute()
        else:
            share = Share.create(title=title,
                                 markdown=markdown,
                                 sharetype=sharetype,
                                 user_id=self.current_user["user_id"], )
            User.update(
                user_leaf=F('user_leaf') + 10).where(
                    id=self.current_user["user_id"]).execute()
            id = str(share.id)
        self.redirect("/share/" + str(id))


class EntryHandler(BaseHandler):
    def get(self, id):
        try:
            share = Share.get(id=id)
        except:
            self.redirect("/404")
        share.markdown = markdown.markdown(share.markdown)
        if self.current_user:
            share.is_liking = Like.select().where(
                share_id=share.id,
                user_id=self.current_user["user_id"]).count() > 0
        comments = Comment.select().where(share_id=share.id)
        for comment in comments:
            user = User.get(id=comment.user_id)
            comment.name = user.user_name
            comment.domain = user.user_domain
            comment.gravatar = get_avatar(user.user_email, 50)
        Share.update(
            hitnum=F('hitnum') + 1).where(id=share.id).execute()
        if self.current_user:
            is_hitted = Hit.select().where(
                share_id=share.id,
                user_id=self.current_user["user_id"]).count() > 0
            Hit.create(
                hitnum=1, share_id=share.id,
                user_id=self.current_user["user_id"],)
        else:
            is_hitted = self.get_cookie(share.id)
            if not is_hitted:
                self.set_cookie(str(share.id), "1")
        posts = Share.select()
        suggest = {}
        for post in posts:
            post.score = 100 + post.id - post.user_id + post.commentnum * 3
            post.score += post.likenum * 4 + post.hitnum * 0.01
            post.score += randint(1, 999) * 0.001
            if post.sharetype == share.sharetype:
                post.score += 5
            if self.current_user:
                is_hitted = Hit.select().where(
                    share_id=post.id,
                    user_id=self.current_user["user_id"]).count() > 0
            else:
                is_hitted = self.get_cookie(share.id)
            if is_hitted:
                post.score -= 50
            suggest[post.score] = post.id
            print(post.id)
            print(post.score)
        realsuggest = []
        i = 1
        for key in sorted(suggest.iterkeys(), reverse=True):
            post = Share.get(id=suggest[key])
            share_post = {
                'id': post.id,
                'title': post.title, }
            realsuggest.append(share_post)
            i = i + 1
            if i > 3:
                break
        self.render(
            "sharee.html", share=share, comments=comments,
            realsuggest=realsuggest)


class CommentHandler(BaseHandler):
    def post(self):
        commentbody = self.get_argument("commentbody", None)
        share_id = self.get_argument("share_id", None)
        html = markdown.markdown(commentbody)
        Comment.create(
            user_id=self.current_user["user_id"],
            share_id=share_id, commentbody=commentbody)
        Share.update(
            commentnum=F('commentnum') + 1).where(id=share_id).execute()
        name = tornado.escape.xhtml_escape(self.current_user["user_name"])
        gravatar = get_avatar(self.current_user["user_email"], 50)
        newcomment = ''
        newcomment += ' <div class="comment">'
        newcomment += '<div class="avatar">'
        newcomment += '<img src="' + gravatar + '" />'
        newcomment += '</div>'
        newcomment += '<div class="name">' + name + '</div>'
        newcomment += '<div class="date" title="at"></div>'
        newcomment += html
        newcomment += '</div>'
        self.write(newcomment)


class LikeHandler(BaseHandler):
    def post(self):
        share_id = self.get_argument("share_id", None)
        likenum = self.get_argument("likenum", 0)
        Like.create(
            user_id=self.current_user["user_id"],
            share_id=share_id)
        share = Share.get(id=share_id)
        Share.update(
            likenum=F('likenum') + 1).where(id=share_id).execute()
        User.update(
            user_leaf=F('user_leaf') + 4).where(id=share.user).execute()
        User.update(
            user_leaf=F('user_leaf') + 2).where(
                id=self.current_user["user_id"]).execute()
        likenum = int(likenum) + 1
        newlikes = ':) ' + str(likenum)
        self.write(newlikes)


class FeedHandler(BaseHandler):
    def get(self):
        shares = Share.select()
        self.set_header("Content-Type", "application/atom+xml")
        self.render("feed.xml", shares=shares)
