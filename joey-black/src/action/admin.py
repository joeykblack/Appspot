'''
Created on Jun 8, 2010
@author auser
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from util import util
from model.blog import Entry, Tag, TagedEntry
from model.user import Minime

class Admin(webapp.RequestHandler):
    def get(self):
        
        action=self.request.get('action')
        if action=='dropdb':
            dropdb()
            
        lusers=Minime.all().fetch(100)
        
        template_values = {
                           'lusers':lusers
            }

        
        template_values.update(util.loadstd(self))
        path = os.path.join(os.path.dirname(__file__), '../html/admin.html')
        self.response.out.write(template.render(path, template_values))
        
        
        
    def post(self):
        
        lusers=Minime.all().fetch(100)
        
        votes=self.request.get_all('votes')
        for vote, luser in zip(votes, lusers):
            luser.votes=int(vote)
            luser.put()
        
        template_values = {
                           'lusers':lusers
            }

        template_values.update(util.loadstd(self))
        path = os.path.join(os.path.dirname(__file__), '../html/admin.html')
        self.response.out.write(template.render(path, template_values))
        
        
        
def dropdb():
    for tagedEntry in TagedEntry.all().fetch(100):
        tagedEntry.delete()
    for entry in Entry.all().fetch(100):
        entry.delete()
    for tag in Tag.all().fetch(100):
        tag.delete()
    for luser in Minime.all().fetch(100):
        luser.delete()