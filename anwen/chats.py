# -*- coding:utf-8 -*-
"""Simplified chat demo for websockets.

Authentication, error handling, etc are left as an exercise for the reader :)
"""

import logging
import tornado.escape
import tornado.websocket
import uuid

from base import BaseHandler


class ChatsHandler(BaseHandler):
    def get(self):
        # if not self.current_user:
        #     self.redirect("/login")
        #     return
        try:
            name = tornado.escape.xhtml_escape(self.current_user["user_name"])
        except:
            name = 'guest'
        self.render("chats.html", name=name, messages=ChatSocketHandler.cache)


class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 200

    def allow_draft76(self):
        # for iOS 5.0 Safari
        return True

    def open(self):
        ChatSocketHandler.waiters.add(self)

    def on_close(self):
        ChatSocketHandler.waiters.remove(self)

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r", message)
        parsed = tornado.escape.json_decode(message)
        chat = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"], }
        chat["html"] = self.render_string("chatsmessage.html", message=chat)

        ChatSocketHandler.update_cache(chat)
        ChatSocketHandler.send_updates(chat)
