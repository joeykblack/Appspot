from google.appengine.ext import webapp
from util import shared
import os

class Index(webapp.RequestHandler):
    
    
    def get(self):
        
        template_values = {
                           }
        path = os.path.join(os.path.dirname(__file__), '../html/index.html')
        shared.render(self, path, template_values)