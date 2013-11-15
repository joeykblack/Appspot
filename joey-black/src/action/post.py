'''
Created on Jun 3, 2010
@author auser
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from form.blog import EntryForm
from util import util
from model.blog import Entry, Tag, TagedEntry
import model
from action import index

class Post(webapp.RequestHandler):
    
    def get(self):
        
        template_values = {
                'entryform':EntryForm()
            }

        template_values.update(util.loadstd(self))
        path = os.path.join(os.path.dirname(__file__), '../html/post.html')
        self.response.out.write(template.render(path, template_values))
    
    
    def post(self):
        
        util.saveEntry(self)
        
        # finish up
        index.doindex(self)