import os
from google.appengine.ext import webapp
from util import shared

class Collection(webapp.RequestHandler):
    
    
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), '../html/collection.html')
        shared.render(self, path, template_values)