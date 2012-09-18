# -*- coding: utf-8 -*- 
# AUTHOR: askender <askender43@gmail.com>
# FILE: handlers.py
# CREATED: 2012-08-28 17:53:10
# MODIFIED: 2012-09-18 22:01:17
# DESCRIPTION: URL Route

from .index import RedirectHandler, IndexHandler, SpecialHandler, NodeHandler
from .user import LoginHandler, JoinusHandler, LogoutHandler, UserhomeHandler, UserlikeHandler, SettingHandler, ChangePassHandler, MemberHandler
from .share import ShareHandler, EntryHandler, CommentHandler, LikeHandler, FeedHandler
from .chat import ChatHandler, MessageNewHandler, MessageUpdatesHandler
from .chats import ChatsHandler, ChatSocketHandler

handlers = [
    (r"/", IndexHandler),
    (r"/about",SpecialHandler),
    (r"/changelog",SpecialHandler),
    (r"/help",SpecialHandler),
    (r"/markdown", SpecialHandler),
    (r"/nodes", SpecialHandler),
    (r"/node/([^/]+)", NodeHandler),

    (r"/user/([^/]+)", UserhomeHandler),
    (r"/userlike/([^/]+)", UserlikeHandler),
    (r"/member", MemberHandler),

    (r"/share", ShareHandler),
    (r"/sharecomment", CommentHandler),
    (r"/sharelike", LikeHandler),
    (r"/share/([^/]+)", EntryHandler),
    (r"/feed", FeedHandler),

    (r"/login", LoginHandler),
    (r"/joinus", JoinusHandler),
    (r"/logout", LogoutHandler),
    (r'/setting', SettingHandler), 
    (r'/changepass', ChangePassHandler), 

    (r"/chat", ChatHandler),
    (r"/a/message/new", MessageNewHandler),
    (r"/a/message/updates", MessageUpdatesHandler),
    (r"/chats", ChatsHandler),
    (r"/chatsocket", ChatSocketHandler),

    (r'/(.*)', RedirectHandler),  # always put this at last

]