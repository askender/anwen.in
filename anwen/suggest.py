# -*- coding:utf-8 -*-

from utils.fliter import *
from utils.avatar import *
from random import randint
from base import JSONHandler


class LikesuggestHandler(JSONHandler):
    def get(self, id):
        try:
            post = Share.get(id=id)
        except:
            self.redirect("/404")
        shares = Share.select()
        suggest = {}
        for share in shares:
            share.score = 100 + share.id - share.user_id + share.commentnum * 3
            share.score += share.likenum * 4 + share.hitnum * 0.01
            share.score += randint(1, 999) * 0.001
            if share.sharetype == post.sharetype:
                share.score += 5
            suggest[share.score] = share.id
        realsuggest = []
        for key in sorted(suggest.iterkeys(), reverse=True):
            share = Share.get(id=suggest[key])
            #share_post = {share.id:share.title}
            share_post = {
                'id': share.id,
                'title': share.title, }
            realsuggest.append(share_post)
        self.write_json(realsuggest)


class DislikesuggestHandler(JSONHandler):
    def get(self):
        pass
