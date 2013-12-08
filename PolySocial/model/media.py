'''
Created on May 31, 2012

@author: joey
'''
from google.appengine.ext.db import polymodel
from google.appengine.ext import db
from model.latest import LatestMixin

class Media(LatestMixin, polymodel.PolyModel):
    ORDER_FIELD = 'timestamp'
    mykey=db.StringProperty()
    title=db.StringProperty()
    text=db.TextProperty()
    link=db.URLProperty()
    timestamp=db.DateTimeProperty(auto_now_add=True)
    tweeted=db.BooleanProperty()
    # comments = list of comment roots
    
    
    def __eq__(self, other):
        return (self.key==other.key)