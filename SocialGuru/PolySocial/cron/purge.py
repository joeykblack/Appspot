'''
Created on Jun 7, 2012

@author: joey
'''
from google.appengine.ext import webapp
from model.story import Story
from model.video import Video


class Purge(webapp.RequestHandler):
    def get(self):
        stories=Story.all().order('-timestamp').fetch(1000, offset=0)
        for story in stories:
            story.delete()
        videos=Video.all().order('-timestamp').fetch(1000, offset=0)
        for video in videos:
            video.delete()
