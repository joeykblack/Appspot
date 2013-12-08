import os
from google.appengine.ext import webapp
from util import shared
from model.story import Story
from model.video import Video

class Index(webapp.RequestHandler):
    
    
    def get(self):
        stories=[]
        for s in Story.all().order('-timestamp').fetch(100):
            stories.append(s)
        videos=[]
        for v in Video.all().order('-timestamp').fetch(100):
            videos.append(v)
        
        template_values = {
                           "stories":stories,
                           "videos":videos
                           }
        path = os.path.join(os.path.dirname(__file__), '../html/index.html')
        shared.render(self, path, template_values)