# -*- coding: utf-8 -*- 

import os.path

import tornado.database
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


from settings import *
from anwen.handlers import handlers
from anwen.uimodules import EntryModule, UseradminModule

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


def main():
    #tornado.locale.load_translations(
        #os.path.join(os.path.dirname(__file__), "_locale"))
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
     main()