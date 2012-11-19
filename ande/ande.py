# -*- coding:utf-8 -*-

from anwen.base import BaseHandler
from db.models import Ande
from andesay import AndeSay
import say


class AndeHandler(BaseHandler):

    def get(self):
        _ = self.locale.translate
        msg = _(say.firstmeet())
        msg = msg + say.expression()
        self.render("ande.html", say=msg)

    def post(self):
        usersay = self.get_argument("ask0", '')
        print usersay
        a = AndeSay()
        andesay = a.get_andesay(usersay)
        user_ip = self.request.remote_ip
        andesay += '<br/>your ip:' + user_ip
        andesay += '<br/>'

        user_id = ''
        if self.current_user:
            user_id = self.current_user["user_id"]
        if not user_id:
            user_id = a.user_ip().replace('.', '')
        Ande.create(
            user_id='1',
            usersay=usersay,
            andesay=andesay, )
        print andesay
        self.write(andesay)
