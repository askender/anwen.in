# -*- coding:utf-8 -*-
import tornado.escape
import urllib2
from settings import *
from base import *

from andes.andesay import AndeSay

class AndeHandler(BaseHandler):
    def get(self):
        self.render("ande.html")

    def post(self):
        uri = self.request.body
        mydict = {}
        for i in uri.split('&'):
            data = i.split('=')
            mydict[data[0]]=data[1]
        usersay = urllib2.unquote(str(mydict['ask0'])).decode("utf-8")
        a = AndeSay()
        andesay = a.get_andesay(usersay)
        user_id = ''
        if self.current_user:
            user_id = self.current_user["user_id"]
        if not user_id:
            user_id = a.get_ip().replace('.', '')
        log_id = self.db.execute(
            "INSERT INTO ande (user_id,usersay,andesay, "
            "chattime) VALUES (%s,%s,%s,UTC_TIMESTAMP())",
            user_id, usersay, andesay)
        debug = True
        # if debug:
        #     andesay += '<br/>'+user()
        #andesay += usersay
        self.write(andesay)