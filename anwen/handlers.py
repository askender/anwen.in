# -*- coding: utf-8 -*- 

from .index import RedirectHandler, NotyetHandler, IndexHandler, SpecialHandler, NodeHandler
from .user import LoginHandler, JoinusHandler, LogoutHandler, UserhomeHandler, UserlikeHandler, SettingHandler, ChangePassHandler, MemberHandler
from .share import ShareHandler, EntryHandler, CommentHandler, LikeHandler, FeedHandler
from .ande import AndeHandler
from .chat import ChatHandler, MessageNewHandler, MessageUpdatesHandler
from .chats import ChatsHandler, ChatSocketHandler

handlers = [
    (r"/", IndexHandler),
    (r"/404", NotyetHandler),
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

    (r'/ande', AndeHandler), 

    (r"/chat", ChatHandler),
    (r"/a/message/new", MessageNewHandler),
    (r"/a/message/updates", MessageUpdatesHandler),

    (r"/chats", ChatsHandler),
    (r"/chatsocket", ChatSocketHandler),

    (r'/(.*)', RedirectHandler),  # always put this at last

]