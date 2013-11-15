'''
Created on Jun 4, 2010
@author joeykblack
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from util import util

class About(webapp.RequestHandler):
    def get(self):
        
        
        template_values = {
            }
        template_values.update(util.loadstd(self))

        path = os.path.join(os.path.dirname(__file__), '../html/about.html')
        self.response.out.write(template.render(path, template_values))