from google.appengine.ext import webapp
from util import shared
import os
from google.appengine.api import users
from model.person import Person

class Profile(webapp.RequestHandler):
    
    
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), '../html/profile.html')
        shared.render(self, path, template_values)
        
    def post(self):
        person=Person.all().filter('user = ', users.get_current_user()).get()
        person.displayname=self.request.get('displayname')
        person.brandname=self.request.get('brandname')
        person.save()
        self.get()
        
        
        