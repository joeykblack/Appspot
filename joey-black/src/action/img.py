'''
Created on Jun 4, 2010
@author joeykblack
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db

class Image(webapp.RequestHandler):
    def get(self):
        entry=db.get(self.request.get("img_id"))
        if entry.img:
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(entry.img)
        else:
            self.error(404)