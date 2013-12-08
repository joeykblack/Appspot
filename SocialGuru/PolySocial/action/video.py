import os
from google.appengine.ext import webapp
from util import shared
import model
import logging

class Video(webapp.RequestHandler):
    
    
    def get(self):
        videos=[]
#        tags=set()
        categories=set()
        
        cat=self.request.get('cat')
        logging.info(cat)
        vids=model.video.Video.all().order('-timestamp')
        
        for v in vids.fetch(100):
#            tags=tags.union(set(v.tags))
            categories=categories.union(set(v.categories))
        
        if cat:
            vids.filter("categories = ", cat)
            
        for v in vids.fetch(100):
            videos.append(v)
        
        template_values = {
                           "videos":videos,
#                           "tags":tags,
                           "categories":categories
                           }
        path = os.path.join(os.path.dirname(__file__), '../html/video.html')
        shared.render(self, path, template_values)
        
        
