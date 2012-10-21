# -*- coding: utf-8 -*-
debug = True
default_platform = 'linux'

db = {
    'name': 'anwen-test'
}

port = 9999
web_server = dict(
    template_path='templates',
    static_path='static',
    locale_path='locale',
    xsrf_cookies=True,
    cookie_secret="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    login_url="/googlelogin",
    autoescape=None,
    debug=debug,
)
