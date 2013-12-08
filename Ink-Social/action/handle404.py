import os
from google.appengine.ext import webapp
from util import shared

class Handle404(webapp.RequestHandler):
    
    
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), '../html/404.html')
        shared.render(self, path, template_values)