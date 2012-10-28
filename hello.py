#!/usr/bin/env python
# -*- coding: utf-8 -*-
import options
import argparse
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from log import logger
from options.url import handlers
from anwen.uimodules import EntryModule, UseradminModule


class Application(tornado.web.Application):
    def __init__(self):
        options.web_server.update(dict(
            ui_modules={"Entry": EntryModule, "Useradmin": UseradminModule},
        ))
        application = tornado.web.Application.__init__(
            self, handlers, **options.web_server)

options.web_server.update(
    dict(ui_modules={"Entry": EntryModule, "Useradmin": UseradminModule},))
application = tornado.web.Application(handlers, **options.web_server)


def create_db():
    import db.models
    db.models.main()
    logger.info('create db success')


def launch():
    tornado.locale.load_translations(options.web_server['locale_path'])
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    logger.info('Server started on %s' % options.port)
    tornado.ioloop.IOLoop.instance().start()


parser = argparse.ArgumentParser(description='Anwen Server')

parser.add_argument(
    '-c', '--create-db',
    dest='extra_operations',
    action='append_const',
    const=create_db,
    help='create database'
)


if __name__ == '__main__':
    args = parser.parse_args()
    [op() for op in args.extra_operations or []]
    launch()
