# -*- coding:utf-8 -*-

from anwen.base import BaseHandler
from db.models import Ande
from andesay import AndeSay
from firstmeet import sayfirstmeet


class AndeHandler(BaseHandler):
    def get(self):
        print sayfirstmeet()
        self.render("ande.html", say=sayfirstmeet())

    def post(self):
        usersay = self.get_argument("ask0", '')
        a = AndeSay()
        andesay = a.get_andesay(usersay)
        user_id = ''
        if self.current_user:
            user_id = self.current_user["user_id"]
        if not user_id:
            user_id = a.user_ip().replace('.', '')
        Ande.create(
            user_id='1',
            usersay=usersay,
            andesay=andesay, )
        self.write(andesay)
