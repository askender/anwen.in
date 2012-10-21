# -*- coding: utf-8 -*- 

from anwen.index import ErrorHandler, NotyetHandler, IndexHandler, SpecialHandler, NodeHandler
from anwen.user import LoginHandler, JoinusHandler, LogoutHandler, UserhomeHandler, UserlikeHandler, SettingHandler, ChangePassHandler, MemberHandler
from anwen.share import ShareHandler, EntryHandler, CommentHandler, LikeHandler, FeedHandler
from anwen.suggest import LikesuggestHandler,DislikesuggestHandler
from ande.ande import AndeHandler
from anwen.chat import ChatHandler, MessageNewHandler, MessageUpdatesHandler
from anwen.chats import ChatsHandler, ChatSocketHandler

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

    (r"/likesuggest/([^/]+)", LikesuggestHandler),
    (r"/dislikesuggest/([^/]+)", DislikesuggestHandler),

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

    # Custom 404 ErrorHandler,always put this at last
    (r'/(.*)', ErrorHandler), 

]