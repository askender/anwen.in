# -*- coding:utf-8 -*-

from base import BaseHandler
from models import Ande
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
            user_id = a.user_ip().replace('.', '')
        log = Ande.create(
                        user_id = '1',
                        usersay = usersay,
                        andesay = andesay,
                    )
        self.write(andesay)