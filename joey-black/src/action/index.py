'''
Created on Jun 3, 2010
@author joeykblack
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from util import util
from model.blog import Entry, TagedEntry, Tag

class Index(webapp.RequestHandler):
    def get(self):
        doindex(self)
        
def doindex(handler):
    tagname=handler.request.get('tag')
    entries=[]
    if tagname:
        tag=Tag.all().filter('name = ', tagname).get()
        if tag and tag.tagedEntries:
            for tagedEntry in tag.tagedEntries:
                if not(tagedEntry.entry.cparent) and tagedEntry.entry.user and tagedEntry.entry.user.nickname()=='JoeyKBlack':
                    entries.append(tagedEntry.entry)
    else:
        for entry in Entry.all().fetch(100):
            if not(entry.cparent) and entry.user and entry.user.nickname()=='JoeyKBlack':
                entries.append(entry)
    entries.reverse()
    
    util.imageafi(entries)
    
    template_values = {
            'entries':entries,
            'ispost':users.is_current_user_admin(),
            'filters':util.filters('')
        }

    template_values.update(util.loadstd(handler))

    path = os.path.join(os.path.dirname(__file__), '../html/index.html')
    handler.response.out.write(template.render(path, template_values))
    

    