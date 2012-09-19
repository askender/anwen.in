# -*- coding:utf-8 -*-

import tornado.escape

# import memcache
# mc = memcache.Client(['127.0.0.1:11211'], debug=0)

from utils.fliter import *
from utils.avatar import *
from settings import *
from base import *



class RedirectHandler(BaseHandler):
    def get(self):
        pass

class IndexHandler(BaseHandler):
    def get(self):
        page = self.get_argument("page", "1")
        sharesum = self.db.execute_rowcount("SELECT * FROM shares")
        sharesum = (sharesum+9)/10
        realpage = str((int(page)-1)*10)
        sharessql = "SELECT * FROM shares ORDER BY id DESC LIMIT "+realpage+",10"
        shares = self.db.query(sharessql)
        # key = 'sharessql'
        # shares = mc.get(key)
        # if not shares:
        #     shares = self.db.query(sharessql)
        #     mc.set(key,shares,60*5) #存5分钟
        sharenum = len(shares)
        for i in range(0,sharenum):
            user = self.get_user_byid(shares[i]['author_id'])
            shares[i]["name"] = user.user_name
            shares[i]['domain'] = user.user_domain
            shares[i]['html'] = filter_tags(shares[i]['html'])[:100]
            shares[i]['gravatar'] = get_avatar(user.user_email,16)
        members = self.db.query("SELECT `user_id`,`user_name`,`user_domain` FROM `users` "
                                "ORDER BY user_id DESC LIMIT 20")
        membernum = len(members)
        if membernum >20:
            membernum = 21
        for i in range(0,membernum):
            user = self.get_user_byid(shares[i]['author_id'])
            members[i]['gravatar'] = get_avatar(user.user_email,35)
        self.render("index.html",shares=shares,members=members,sharesum=sharesum,page=page)


class SpecialHandler(BaseHandler):
    def get(self):
        #host = self.request.headers['Host']
        realpath = self.request.path[1:]
        share = self.db.get("SELECT * FROM shares WHERE slug = %s",realpath)
        if not share: raise tornado.web.HTTPError(404)
        comments = self.db.query("SELECT * FROM comments WHERE share_id = %s ORDER BY id DESC", share.id)
        commentnum = len(comments)
        for i in range(0,commentnum):
            user = self.get_user_byid(comments[i]['author_id'])
            comments[i]["name"] = user.user_name
            comments[i]['domain'] = user.user_domain
            comments[i]['gravatar'] = get_avatar(user.user_email,50)
        self.render("sharee.html", share=share,comments=comments)


class NodeHandler(BaseHandler):
    def get(self,node):
        page = self.get_argument("page", "1")
        sharesum = self.db.execute_rowcount("SELECT * FROM shares where sharetype = %s",node)
        sharesum = (sharesum+9)/10
        shares = self.db.query("SELECT * FROM shares where sharetype = %s ORDER BY published "
                                "DESC LIMIT %s,10",node,(int(page)-1)*10)
        if not shares: raise tornado.web.HTTPError(404)
        sharenum = len(shares)
        for i in range(0,sharenum):
            user = self.get_user_byid(shares[i]['author_id'])
            shares[i]["name"] = user.user_name
            shares[i]['domain'] = user.user_domain
            shares[i]['html'] = filter_tags(shares[i]['html'])[:50]
            shares[i]['gravatar'] = get_avatar(user.user_email,16)
        members = self.db.query("SELECT `user_id`,`user_name`,`user_domain` FROM `users` "
                                "ORDER BY user_id DESC LIMIT 20")
        membernum = len(members)
        if membernum >20:
            membernum = 21
        for i in range(0,membernum):
            user = self.get_user_byid(shares[i]['author_id'])
            members[i]['gravatar'] = get_avatar(user.user_email,35)
        self.render("node.html",shares=shares,members=members,sharesum=sharesum,page=page)