'''
Created on May 29, 2012

@author: joey
'''

from google.appengine.ext import db
from model import media

class Video(media.Media):
    img=db.URLProperty()
    imgBig=db.URLProperty()
    tags=db.StringListProperty()
    categories=db.StringListProperty()