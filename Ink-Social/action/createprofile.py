from google.appengine.ext import webapp
from util import shared
import os
from google.appengine.api import users
from model.person import Person

class CreateProfile(webapp.RequestHandler):
    
    
    def get(self):
        user=users.get_current_user()
        template_values = {
                            'user':user
                           }
        path = os.path.join(os.path.dirname(__file__), '../html/createprofile.html')
        shared.render(self, path, template_values)
        
    def post(self):
        person=Person()
        person.displayname=self.request.get('displayname')
        person.brandname=self.request.get('brandname')
        person.user=users.get_current_user()
        person.save()
        self.redirect('/profile')
        
        
        