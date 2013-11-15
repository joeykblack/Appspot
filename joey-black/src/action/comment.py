'''
Created on Jun 7, 2010
@author auser
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from model.blog import Entry, Tag, TagedEntry
from form.blog import EntryForm
from util import util
import model
from action import delete, index

class Comment(webapp.RequestHandler):
    def get(self):
        key=self.request.get('topkey')
        if key:
            entry=Entry.get(key)
        else:
            index.doindex(self)
            return
        
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
        deleted=False
        if deletekey:
            deleteentry=Entry.get(deletekey)
            if  deleteentry:
                delete.deleteEntry(deleteentry)
                deleted=True
        
        template_values = {
                'editkey':editkey,
                'up':up(entry),
                'deleleted':deleted,
                'comments':commentsHtml(top=entry,entry=entry),
                'entryform':entryform,
                'topkey':key,
                'tags':tags
            }


        template_values.update(util.loadstd(self))
        path = os.path.join(os.path.dirname(__file__), '../html/comments.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        key=self.request.get('topkey')
        entry=Entry.get(key)
        
        util.saveEntry(self)
        
        template_values = {
                'up':up(entry),
                'comments':commentsHtml(top=entry,entry=entry),
                'entryform':EntryForm(),
                'topkey':key
            }

        template_values.update(util.loadstd(self))
        path = os.path.join(os.path.dirname(__file__), '../html/comments.html')
        self.response.out.write(template.render(path, template_values))
        
        
        


def up(entry):
    if entry and entry.cparent:
        link='<a href="/comment?topkey='+str(entry.cparent.key())+'">up</a>'
    else:
        link=''
    return link

    
def commentsHtml(top, entry):
    html='<li>'
    html+='<h2>'+entry.title+'</h2>'
    posted=str(entry.posted)
    html+='<h5>posted by '+entry.by+' on '+posted+'</h5>'
    html+='<p>'+util.imageafiText(entry)+'</p>'
    html+='<p>'
    if entry.comments:
        length=str(len(entry.comments.fetch(100)))
        html+='<a href=/comment?topkey='+str(entry.key())+'>Comments('+length+')</a><br />'
    user=users.get_current_user()
    if user:
        if user.nickname()==entry.by:
            html+='<a href="/comment?topkey='+str(top.key())+'&editkey='+str(entry.key())+'">Edit</a> | <a href="/comment?topkey='+str(top.key())+'&deletekey='+str(entry.key())+'">Delete</a>'
        if users.is_current_user_admin():
            html+=' | <a href="/comment?topkey='+str(top.key())+'&deletekey='+str(entry.key())+'">Admin Delete</a>'
    html+='</p>'
    html+='<hr />'
    if entry.comments:
        html+='<ul>'
        for e in entry.comments:
            html+=commentsHtml(top=top, entry=e)
        html+='</ul>'
    html+='</li>'
    return html
    
    
    
    
    
    
    
    