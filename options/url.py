# -*- coding: utf-8 -*-

from anwen.index import IndexHandler, SpecialHandler, NodeHandler, NotyetHandler
from anwen.user import LoginHandler, JoinusHandler, LogoutHandler, UserhomeHandler, UserlikeHandler, SettingHandler, ChangePassHandler, MemberHandler
from anwen.share import ShareHandler, EntryHandler, CommentHandler, LikeHandler, FeedHandler
from anwen.suggest import LikesuggestHandler, DislikesuggestHandler
from ande.ande import AndeHandler
from anwen.talk import TalkHandler, ChatSocketHandler, MessageNewHandler, MessageUpdatesHandler

handlers = [
    (r"/", IndexHandler),
    (r"/404", NotyetHandler),
    (r"/about", SpecialHandler),
    (r"/changelog", SpecialHandler),
    (r"/help", SpecialHandler),
    (r"/markdown", SpecialHandler),
    (r"/ande-growup-log", SpecialHandler),
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

    (r"/chat", TalkHandler),
    (r"/chats", TalkHandler),
    (r"/talk", TalkHandler),
    (r"/chatsocket", ChatSocketHandler),
    (r"/a/message/new", MessageNewHandler),
    (r"/a/message/updates", MessageUpdatesHandler),



    # Custom 404 NotyetHandler,always put this at last
    (r'/(.*)', NotyetHandler),

]
