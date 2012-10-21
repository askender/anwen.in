#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from logging import getLogger, NOTSET, info
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import enable_pretty_logging
import options
from options.url import handlers
from anwen.uimodules import EntryModule, UseradminModule


class Application(tornado.web.Application):
    def __init__(self):
        options.web_server.update(dict(
            ui_modules={"Entry": EntryModule,"Useradmin": UseradminModule},
        ))
        tornado.web.Application.__init__(self, handlers, **options.web_server)


def launch():
    tornado.locale.load_translations(options.web_server['locale_path'])
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    info('Server started on %s' % options.port)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == '__main__':
    enable_pretty_logging()
    getLogger().setLevel(NOTSET)
    launch()