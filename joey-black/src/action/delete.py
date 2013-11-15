'''
Created on Jun 4, 2010
@author auser
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from action import index

class DeleteEntry(webapp.RequestHandler):
    def get(self):
        key=self.request.get('key')
        entry=db.get(key)
        
        deleteEntry(entry)
        
        index.doindex(self)
        
def deleteEntry(entry):
    if entry:
        for tagedEntry in entry.tagedEntries:
            if len(tagedEntry.tag.tagedEntries.fetch(100))==1:
                tagedEntry.tag.delete() 
            tagedEntry.delete()
        
        for comment in entry.comments:
            deleteEntry(comment)
        
        entry.delete()