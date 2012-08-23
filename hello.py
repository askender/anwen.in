# -*- coding:utf-8 -*-
import os.path

import tornado.database
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import share,user,index,post,chat, chats
from settings import *
from base import *

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            site_title=u"Anwen",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            locale_path=os.path.join(os.path.dirname(__file__), "_locale"),
            ui_modules={"Entry": EntryModule,"Userinfo": UserinfoModule},
            xsrf_cookies=True,
            cookie_secret="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/googlelogin",
            autoescape=None,
            debug=True,
        )

        handlers = [
            (r"/", index.IndexHandler),
            (r"/index.html", index.IndexHandler),
            (r"/about",index.SpecialHandler),
            (r"/changelog",index.SpecialHandler),
            (r"/help",index.SpecialHandler),
            (r"/markdown", index.SpecialHandler),

            (r"/user/([^/]+)", user.UserhomeHandler),
            (r"/userlike/([^/]+)", user.UserlikeHandler),

            (r"/share", share.IndexHandler),
            (r"/sharecomment", share.CommentHandler),
            (r"/sharelike", share.LikeHandler),
            (r"/share/([^/]+)", share.EntryHandler),
            (r"/feed", share.FeedHandler),

            (r"/login", user.LoginHandler),
            (r"/joinus", user.JoinusHandler),
            (r"/logout", user.LogoutHandler),

            (r"/chat", chat.ChatHandler),
            (r"/a/message/new", chat.MessageNewHandler),
            (r"/a/message/updates", chat.MessageUpdatesHandler),
            (r"/chats", chats.ChatsHandler),
            (r"/chatsocket", chats.ChatSocketHandler),

            (r"/(favicon\.ico)", tornado.web.StaticFileHandler,dict(path=settings['static_path'])),
            (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler,dict(path=settings['static_path'])),
            #(r"/(.*)", index.UrlHandler),
        ]



        tornado.web.Application.__init__(self, handlers, **settings)

        self.db = tornado.database.Connection(
            host=options.host, database=options.database,
            user=options.user, password=options.password)


class EntryModule(tornado.web.UIModule):
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)

class UserinfoModule(tornado.web.UIModule):
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
        return self.render_string("modules/userinfo.html",name=name,gravatar=gravatar,domain=domain)

def main():
    #tornado.locale.load_translations(
        #os.path.join(os.path.dirname(__file__), "_locale"))
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
     main()