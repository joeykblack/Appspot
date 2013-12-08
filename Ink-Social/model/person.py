'''
Created on Jun 8, 2012

@author: joey
'''
from google.appengine.ext import db

class Person(db.Model):
    user=db.UserProperty()
    displayname=db.StringProperty()
    brandname=db.StringProperty()

        