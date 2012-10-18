# -*- coding:utf-8 -*-

import markdown
from utils.fliter import *
from utils.avatar import *
from base import BaseHandler
from models import User, Share, Comment, Like, Hit
from peewee import F
from random import randint

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
        print(type(shares))
        self.render("index.html",shares=shares,members=members,pagesum=pagesum,page=page)


class SpecialHandler(BaseHandler):
    def get(self):
        realpath = self.request.path[1:]
        try:
            share = Share.get(slug = realpath)
        except:
            self.redirect("/404")
        share.markdown = markdown.markdown(share.markdown)
        if self.current_user:
            share.is_liking = Like.select().where(share_id=share.id,user_id=self.current_user["user_id"]).count()>0
        comments = Comment.select().where(share_id=share.id)
        for comment in comments:
            user = User.get(id = comment.user_id)
            comment.name = user.user_name
            comment.domain = user.user_domain
            comment.gravatar = get_avatar(user.user_email,50)
        hit = Share.update(hitnum = F('hitnum') +1).where(id = share.id).execute()
        if self.current_user:
            is_hitted = Hit.select().where(share_id=share.id,user_id=self.current_user["user_id"]).count()>0
            userhit = Hit.create(hitnum = 1,
                                share_id = share.id,
                                user_id = self.current_user["user_id"],
                )
        else:
            is_hitted = self.get_cookie(share.id)
            if not is_hitted:
                self.set_cookie(str(share.id), "1")
        posts = Share.select()
        suggest = {}
        for post in posts:
            post.score = 100+post.id-post.user_id+post.commentnum*3+post.likenum*4+post.hitnum*0.01+randint(1,999)*0.001
            if post.sharetype == share.sharetype:
                post.score += 5
            if self.current_user:
                is_hitted = Hit.select().where(share_id=post.id,user_id=self.current_user["user_id"]).count()>0
            else:
                is_hitted = self.get_cookie(share.id)
            if is_hitted:
                post.score -= 50
            suggest[post.score] = post.id
            print(post.id)
            print(post.score)
        realsuggest = []
        i = 1
        for key in sorted(suggest.iterkeys(), reverse = True):
            post = Share.get(id=suggest[key])
            share_post = {'id':post.id,
                        'title':post.title,
            }
            realsuggest.append(share_post)
            i = i+1
            if i>3:
                break
        self.render("sharee.html", share=share,comments=comments, realsuggest=realsuggest)


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
        self.render("node.html",shares=shares,members=members,pagesum=pagesum,page=page)
