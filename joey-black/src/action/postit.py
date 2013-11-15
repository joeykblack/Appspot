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
from model.blog import Tag, Entry
from action import index, delete
from form.blog import EntryForm

class Postit(webapp.RequestHandler):
    def get(self):
        
        util.vote(self)
        
        entryform=EntryForm()
        editkey=self.request.get('editkey')
        tags=''
        if editkey:
            editentry=Entry.get(editkey)
            if editentry:
                if editentry.type=='Text':
                    editentry.text=editentry.text.replace('<br />', '\n')
                entryform=EntryForm(instance=editentry)
                for tagged in editentry.tagedEntries:
                    tags+=tagged.tag.name+','
                tags=tags[0:-1] #takes off last char
            
        deletekey=self.request.get('deletekey')
        if deletekey:
            deleteentry=Entry.get(deletekey)
            if  deleteentry:
                delete.deleteEntry(deleteentry)
        
        dopostit(self, entryform=entryform, editkey=editkey, tags=tags)
        
        
    def post(self):
        # save post
        util.saveEntry(self)
        
        dopostit(self)        
        
def dopostit(handler, entryform=EntryForm(), editkey='', tags=''):
    tagname=handler.request.get('tag')
    entries=[]
    if tagname:
        tag=Tag.all().filter('name = ', tagname).get()
        if tag and tag.tagedEntries:
            for tagedEntry in tag.tagedEntries:
                if not(tagedEntry.entry.cparent):
                    entries.append(tagedEntry.entry)
    else:
        for entry in Entry.all().fetch(100):
            if not(entry.cparent):
                entries.append(entry)
    entries.reverse()
    
    util.imageafi(entries)
    
    username=''
    if users.get_current_user():
        username=users.get_current_user().nickname()
    
    template_values = {
                           'currentuser':username,
                           'filters':util.filters('postit'),
                           'entryform':entryform,
                           'entries':entries,
                           'editkey':editkey,
                           'tags':tags
            }

    template_values.update(util.loadstd(handler))
    path = os.path.join(os.path.dirname(__file__), '../html/postit.html')
    handler.response.out.write(template.render(path, template_values))

    
    
    
    
    