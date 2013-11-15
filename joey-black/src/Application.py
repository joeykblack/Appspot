'''
Created on May 24, 2010

@author: joey
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from action.index import Index
from action.post import Post
from action.img import Image
from action.about import About
from action.edit import EditEntry
from action.delete import DeleteEntry
from action.comment import Comment
from action.admin import Admin
from action.postit import Postit
from action.comic import Comic
from action.frame import Frame
from action.research import Research



application = webapp.WSGIApplication(
                                     [('/', Index),
                                      ('/post', Post),
                                      ('/img', Image),
                                      ('/about', About),
                                      ('/edit', EditEntry),
                                      ('/delete', DeleteEntry),
                                      ('/comment', Comment),
                                      ('/admin', Admin),
                                      ('/postit', Postit),
                                      ('/comic', Comic),
                                      ('/frame', Frame),
                                      ('/research', Research)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()