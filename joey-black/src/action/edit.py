'''
Created on Jun 4, 2010
@author auser
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from form.blog import EntryForm
from util import util
from model.blog import Entry

class EditEntry(webapp.RequestHandler):
    def get(self):
        key=self.request.get('editkey')
        entry=Entry.get(key)
        tags=''
        for tagged in entry.tagedEntries:
            tags+=tagged.tag.name+','
        tags=tags[0:-1] #takes off last char
        if entry.type=='Text':
            entry.text=entry.text.replace('<br />', '\n')
        
        template_values = {
                'editkey':key,
                'entryform':EntryForm(instance=entry),
                'tags':tags
            }

        template_values.update(util.loadstd(self))

        path = os.path.join(os.path.dirname(__file__), '../html/post.html')
        self.response.out.write(template.render(path, template_values))