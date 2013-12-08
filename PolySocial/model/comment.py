'''
Created on May 31, 2012

@author: joey
'''
from google.appengine.ext import db
from model.media import Media

class Comment(db.Model):
    title=db.StringProperty()
    by=db.StringProperty()
    text=db.StringProperty()
    op=db.SelfReference(collection_name='comments')
    media=db.ReferenceProperty(Media, collection_name='comments')
    timestamp=db.DateTimeProperty(auto_now_add=True)