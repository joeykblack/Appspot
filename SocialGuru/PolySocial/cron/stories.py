'''
Created on May 29, 2012

@author: joey
'''
from google.appengine.ext import webapp
from cron.gtrend import GTrendCron
from model.story import Story
from cron.ytrend import YTrendCron
from model.video import Video

class Stories(webapp.RequestHandler):
    
    def get(self):
        stories=Story.all().fetch(1000)
        GTrendCron.doCron(stories)     
        videos=Video.all().fetch(1000)
        YTrendCron.doCron(videos)
