from google.appengine.ext import webapp
from model.story import Story
from util import shared
import os

class Article(webapp.RequestHandler):
    
    
    def get(self):
        stories=[]
        for s in Story.all().order('-timestamp').fetch(100):
            stories.append(s)
        
        template_values = {
                           "stories":stories
                           }
        path = os.path.join(os.path.dirname(__file__), '../html/article.html')
        shared.render(self, path, template_values)