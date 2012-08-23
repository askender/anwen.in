# -*- coding:utf-8 -*-
import tornado.escape
from settings import *
from base import *
from fliter import *

class IndexHandler(BaseHandler):
    def get(self):
        shares = self.db.query("SELECT * FROM shares ORDER BY published "
                                "DESC LIMIT 10")
        sharenum = len(shares)
        if sharenum >10:
            sharenum = 11
        for i in range(0,sharenum):
            user = self.db.get("SELECT * FROM `users` WHERE `user_id`=%s", shares[i]['author_id'])
            shares[i]["name"] = user.user_name
            shares[i]['domain'] = user.user_domain
            shares[i]['html'] = filter_tags(shares[i]['html'])[:50]
            shares[i]['gravatar'] = "http://www.gravatar.com/avatar.php?"+urllib.urlencode({'gravatar_id':hashlib.md5(user.user_email.lower()).hexdigest(), 'size':str(16)})
            #shares[1].get("name")
        self.render("index.html", shares=shares)


class SpecialHandler(BaseHandler):
    def get(self):
        #host = self.request.headers['Host']
        realpath = self.request.path[1:]
        share = self.db.get("SELECT * FROM shares WHERE slug = %s",realpath)
        if not share: raise tornado.web.HTTPError(404)
        comments = self.db.query("SELECT * FROM comments WHERE share_id = %s ORDER BY id DESC", share.id)
        commentnum = len(comments)
        for i in range(0,commentnum):
            user = self.db.get("SELECT * FROM `users` WHERE `user_id`=%s", comments[i]['author_id'])
            comments[i]["name"] = user.user_name
            comments[i]['domain'] = user.user_domain
            comments[i]['gravatar'] = "http://www.gravatar.com/avatar.php?"+urllib.urlencode({'gravatar_id':hashlib.md5(user.user_email.lower()).hexdigest(), 'size':str(50)})
        self.render("sharee.html", share=share,comments=comments)