'''
Created on Jun 9, 2010
@author: auser
'''

from google.appengine.ext import db

class Minime(db.Model):
    user=db.UserProperty()
    votes=db.IntegerProperty()