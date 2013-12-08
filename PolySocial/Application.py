'''
Created on May 24, 2012

@author: joey
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from action.index import Index
from action.about import About
from action.article import Article
from action.video import Video
from action.details import Details



application = webapp.WSGIApplication(
                                     [('/', Index),
                                      ('/about', About),
                                      ('/article', Article),
                                      ('/video', Video),
                                      ('/details', Details)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()