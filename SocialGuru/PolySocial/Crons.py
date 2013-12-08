'''
Created on May 24, 2012

@author: joey
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from cron.stories import Stories
from cron.tweet import Tweet
from cron.purge import Purge



application = webapp.WSGIApplication(
                                     [
                                      ('/update/stories', Stories),
                                      ('/update/tweet', Tweet),
                                      ('/update/purge', Purge)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()