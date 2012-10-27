# -*- coding: utf-8 -*-
debug = True

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

log = {
    'log_max_bytes': 5 * 1024 * 1024,  # 5M
    'backup_count': 10,
    'log_path': {
        # logger of running server; DONOT change the name 'logger'
        'logger': 'log/files/server.log',
        # logger of user behavior
        'user_logger': 'log/files/user.log'
    }
}

try:
    from server_setting import *
except:
    pass
