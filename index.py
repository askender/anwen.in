# -*- coding:utf-8 -*-
import tornado.escape
from settings import *
from base import *
from fliter import *

class IndexHandler(BaseHandler):
    def get(self):
        page = self.get_argument("page", "1")
        sharesum = self.db.execute_rowcount("SELECT * FROM shares")
        sharesum = (sharesum+9)/10
        shares = self.db.query("SELECT * FROM shares ORDER BY id "
                                "DESC LIMIT %s,10",(int(page)-1)*10)
        sharenum = len(shares)
        for i in range(0,sharenum):
            user = self.get_user_byid(shares[i]['author_id'])
            shares[i]["name"] = user.user_name
            shares[i]['domain'] = user.user_domain
            shares[i]['html'] = filter_tags(shares[i]['html'])[:50]
            shares[i]['gravatar'] = "http://www.gravatar.com/avatar.php?"+urllib.urlencode({'gravatar_id':hashlib.md5(user.user_email.lower()).hexdigest(), 'size':str(16)})
        members = self.db.query("SELECT `user_id`,`user_name`,`user_domain` FROM `users` "
                                "ORDER BY user_id DESC LIMIT 20")
        membernum = len(members)
        if membernum >20:
            membernum = 21
        for i in range(0,membernum):
            user = self.get_user_byid(shares[i]['author_id'])
            members[i]['gravatar'] = "http://www.gravatar.com/avatar.php?"+urllib.urlencode({'gravatar_id':hashlib.md5(user.user_email.lower()).hexdigest(), 'size':str(35)})
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
            comments[i]['gravatar'] = "http://www.gravatar.com/avatar.php?"+urllib.urlencode({'gravatar_id':hashlib.md5(user.user_email.lower()).hexdigest(), 'size':str(50)})
        self.render("sharee.html", share=share,comments=comments)


class NodeHandler(BaseHandler):
    def get(self,node):
        shares = self.db.query("SELECT * FROM shares where sharetype = %s ORDER BY published "
                                "DESC LIMIT 10",node)
        sharenum = len(shares)
        if sharenum >10:
            sharenum = 11
        for i in range(0,sharenum):
            user = self.get_user_byid(shares[i]['author_id'])
            shares[i]["name"] = user.user_name
            shares[i]['domain'] = user.user_domain
            shares[i]['html'] = filter_tags(shares[i]['html'])[:50]
            shares[i]['gravatar'] = "http://www.gravatar.com/avatar.php?"+urllib.urlencode({'gravatar_id':hashlib.md5(user.user_email.lower()).hexdigest(), 'size':str(16)})
        members = self.db.query("SELECT `user_id`,`user_name`,`user_domain` FROM `users` "
                                "ORDER BY user_id DESC LIMIT 20")
        membernum = len(members)
        if membernum >20:
            membernum = 21
        for i in range(0,membernum):
            user = self.get_user_byid(shares[i]['author_id'])
            members[i]['gravatar'] = "http://www.gravatar.com/avatar.php?"+urllib.urlencode({'gravatar_id':hashlib.md5(user.user_email.lower()).hexdigest(), 'size':str(35)})
        self.render("node.html",shares=shares,members=members)