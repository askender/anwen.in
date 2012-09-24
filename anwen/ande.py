# -*- coding:utf-8 -*-

from base import BaseHandler
from andes.andesay import AndeSay



class AndeHandler(BaseHandler):
    def get(self):
        self.render("ande.html")

    def post(self):
        usersay = self.get_argument("ask0", '')
        a = AndeSay()
        andesay = a.get_andesay(usersay)
        user_id = ''
        if self.current_user:
            user_id = self.current_user["user_id"]
        if not user_id:
            user_id = a.get_ip().replace('.', '')
        # log_id = self.db.execute(
        #     "INSERT INTO ande (user_id,usersay,andesay, "
        #     "chattime) VALUES (%s,%s,%s,UTC_TIMESTAMP())",
        #     user_id, usersay, andesay)
        debug = True
        # if debug:
        #     andesay += '<br/>'+user()
        #andesay += usersay
        self.write(andesay)