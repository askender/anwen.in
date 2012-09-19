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
        
        log_id = self.db.execute(
            "INSERT INTO ande (user_id,usersay,andesay, "
            "chattime) VALUES (%s,%s,%s,UTC_TIMESTAMP())",
            self.current_user["user_id"], usersay, andesay)
        #andesay += usersay
        self.write(andesay)