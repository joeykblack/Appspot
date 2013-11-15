'''
Created on Jun 23, 2010
@author: auser
'''

from google.appengine.ext import db

class Comic(db.Model):
    name=db.StringProperty()
    tip=db.StringProperty()
    owner=db.UserProperty()
    last=db.SelfReferenceProperty(collection_name='nexts')
    text=db.TextProperty()
    date=db.DateTimeProperty(auto_now_add=1)
    
class Frame(db.Model):
    text=db.TextProperty()
    chars=db.StringProperty()
    img=db.BlobProperty()
    last=db.SelfReference(collection_name='kids')
    owner=db.UserProperty()
    comic=db.ReferenceProperty(Comic, collection_name="frames")
    
    #frame sequence
    #format 1x1x1 = 3rd frame
    #1x1x2 = 2nd version of 3rd frame
    frameseq=db.StringProperty() 
    
class Character(db.Model):
    name=db.StringProperty()
    owner=db.UserProperty()
    description=db.TextProperty()
    
class Avatar(db.Model):
    char=db.ReferenceProperty(Character, collection_name="avatars")
    img=db.BlobProperty()
    name=db.StringProperty()