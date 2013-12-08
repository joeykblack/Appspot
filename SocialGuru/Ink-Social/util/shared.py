'''
Created on May 27, 2012

@author: joey
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from model.person import Person


def render(handler, path, template_values):
    person=Person.all().filter('user = ', users.get_current_user()).get()
    template_values.update(loadloginout(handler))
    template_values.update( {
                     'person':person
                     });
                     
    template_values.update( {
                     'content':template.render(path, template_values)
                     });
                     
    shared_path = os.path.join(os.path.dirname(__file__), '../html/shared.html')
    handler.response.out.write(template.render(shared_path, template_values))

def do404(handler):
    path = os.path.join(os.path.dirname(__file__), '../html/404.html')
    template_values={}
    render(handler, path, template_values)
    
def loadloginout(handler):
    user = users.get_current_user()
    if user:
        login_link=users.create_logout_url(handler.request.uri)
        login_text="Logout " + user.nickname()
    else:
        login_link=users.create_login_url(handler.request.uri)
        login_text="Login"

    return {
              "login_link":login_link,
              "login_text":login_text
           }