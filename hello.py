# -*- coding: utf-8 -*- 
# AUTHOR: askender <askender43@gmail.com>
# FILE: hello.py
# CREATED: 2012-08-28 18:05:19
# MODIFIED: 2012-08-28 18:05:23
# DESCRIPTION: Main Server File say hello

import os.path

import tornado.database
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from settings import *
from base import *
from handlers import handlers

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            site_title=u"Anwen",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            locale_path=os.path.join(os.path.dirname(__file__), "_locale"),
            ui_modules={"Entry": EntryModule,"Useradmin": UseradminModule},
            xsrf_cookies=True,
            cookie_secret="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/googlelogin",
            autoescape=None,
            debug=True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        self.db = tornado.database.Connection(
            host=options.host, database=options.database,
            user=options.user, password=options.password)


class EntryModule(tornado.web.UIModule):
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)

class UseradminModule(tornado.web.UIModule):
    def render(self):
        if self.current_user:
            name = tornado.escape.xhtml_escape(self.current_user["user_name"])
            email = tornado.escape.xhtml_escape(self.current_user["user_email"])
            domain = tornado.escape.xhtml_escape(self.current_user["user_domain"])
            gravatar = "http://www.gravatar.com/avatar.php?"+urllib.urlencode({'gravatar_id':hashlib.md5(email.lower()).hexdigest(), 'size':str(16)})
        else:
            name = ''
            gravatar = ''
            domain = ''
        return self.render_string("modules/useradmin.html",name=name,gravatar=gravatar,domain=domain)


def main():
    #tornado.locale.load_translations(
        #os.path.join(os.path.dirname(__file__), "_locale"))
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
     main()