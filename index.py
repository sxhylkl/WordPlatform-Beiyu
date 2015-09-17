#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from semantics import semantics_index
from semantics import semantics_show

import os
home=''
os.environ["SCRIPT_NAME"] = home
os.environ["REAL_SCRIPT_NAME"] = home

urls = (
    "/", "semantics_index",
    "/semantics", "semantics_index",
    "/semantics/show", "semantics_show",
    )
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'This is a project of Beiyu'

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
