# -*- coding:utf-8 -*-

import markdown
from utils.fliter import *
from utils.avatar import *
from base import BaseHandler
from models import User, Share, Comment


class RedirectHandler(BaseHandler):
    def get(self):
        pass


class NotyetHandler(BaseHandler):
    def get(self):
        self.render("404.html")


class IndexHandler(BaseHandler):
    def get(self):
        page = self.get_argument("page", "1")
        realpage = int(page)
        shares = Share.select().order_by(('id','desc')).paginate(realpage, 10)
        sharesum = shares.count()
        pagesum = (sharesum+9)/10
        for share in shares:
            user = User.get(id = share.user_id)
            share.name = user.user_name
            share.domain = user.user_domain
            share.markdown = markdown.markdown(share.markdown)
            share.markdown = filter_tags(share.markdown)[:100]
            share.gravatar = get_avatar(user.user_email,16)
        members = User.select().order_by('id').paginate(1, 20)
        for member in members:
            user = User.get(id = member.id)
            member.gravatar = get_avatar(user.user_email,35)
        self.render("index.html",shares=shares,members=members,sharesum=sharesum,page=page)


class SpecialHandler(BaseHandler):
    def get(self):
        realpath = self.request.path[1:]
        share = Share.get(slug = realpath)
        share.markdown = markdown.markdown(share.markdown)
        if not share: 
            self.redirect("/404")
        comments = Comment.select().where(share_id=share.id)
        for comment in comments:
            user = User.get(id = comment.user_id)
            comment.name = user.user_name
            comment.domain = user.user_domain
            comment.gravatar = get_avatar(user.user_email,50)
        self.render("sharee.html", share=share,comments=comments)


class NodeHandler(BaseHandler):
    def get(self,node):
        page = self.get_argument("page", "1")
        realpage = int(page)
        shares = Share.select().where(sharetype=node).order_by('id').paginate(realpage, 10)
        sharesum = shares.count()
        pagesum = (sharesum+9)/10
        for share in shares:
            user = User.get(id = share.user_id)
            share.name = user.user_name
            share.domain = user.user_domain
            share.markdown = filter_tags(share.markdown)[:100]
            share.gravatar = get_avatar(user.user_email,16)
        members = User.select().order_by('id').paginate(1, 20)
        for member in members:
            user = User.get(id = member.id)
            member.gravatar = get_avatar(user.user_email,35)
        self.render("node.html",shares=shares,members=members,sharesum=sharesum,page=page)
