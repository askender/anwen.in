# -*- coding: UTF-8 -*-

import os.path

config = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    locale_path=os.path.join(os.path.dirname(__file__), "_locale"),
    xsrf_cookies=True,
    cookie_secret="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    login_url="/googlelogin",
    autoescape=None,
    debug=True,
)