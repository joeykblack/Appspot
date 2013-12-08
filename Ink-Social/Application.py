'''
Created on May 24, 2012

@author: joey
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from action.index import Index
from action.about import About
from action.createprofile import CreateProfile
from action.profile import Profile
from action.cardcreator import CardCreator
from action.browse import Browse
from action.collection import Collection
from action.handle404 import Handle404
from action.openclipart import OpenClipart



application = webapp.WSGIApplication(
                                     [('/', Index),
                                      ('/about', About),
                                      ('/createprofile', CreateProfile),
                                      ('/profile', Profile),
                                      ('/cardcreator', CardCreator),
                                      ('/browse', Browse),
                                      ('/collection', Collection),
                                      ('/openclipart', OpenClipart),
                                      ('/.*', Handle404)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()