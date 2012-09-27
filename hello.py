#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from logging import getLogger, NOTSET, info
from tornado.options import enable_pretty_logging

from config import config
from anwen.handlers import handlers
from anwen.uimodules import EntryModule, UseradminModule


class Application(tornado.web.Application):
    def __init__(self):
        config.update(dict(
            ui_modules={"Entry": EntryModule,"Useradmin": UseradminModule},
            #autoescape = None
        ))
        tornado.web.Application.__init__(self, handlers, **config)


def launch():
    tornado.locale.load_translations(config['locale_path'])
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(9999)
    info('Server started')
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    enable_pretty_logging()
    getLogger().setLevel(NOTSET)
    launch()