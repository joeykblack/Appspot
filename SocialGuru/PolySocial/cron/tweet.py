'''
Created on May 29, 2012

@author: joey
'''
from google.appengine.ext import webapp
from model.story import Story
from cron.twitter import twitterCron
import logging



def toHash(mykey):
    h=[]
    for w in mykey.split():
        h.append(w.capitalize())
    h=''.join(h)
    return '#'+h

class Tweet(webapp.RequestHandler):
    
    def get(self):
        story=Story().all().latest()
        msg=toHash(story.mykey) + " " + story.link
        if not story.tweeted:
            story.tweeted=True
            story.save()
            twitterCron.tweet(msg)
        else:
            logging.info('Already tweeted: ' + msg)
        
        
        
        