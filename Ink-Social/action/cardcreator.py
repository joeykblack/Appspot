import os
from google.appengine.ext import webapp
from util import shared

class CardCreator(webapp.RequestHandler):
    
    
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), '../html/cardcreator.html')
        shared.render(self, path, template_values)