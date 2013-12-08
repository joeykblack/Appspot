import os
from google.appengine.ext import webapp
from util import shared
from model.media import Media
from model.comment import Comment
from google.appengine.api import users

class Details(webapp.RequestHandler):
    
    def get(self):
        media=self.getMedia(self.request.get('key'))
        if media:
            template_values = {"media":media}
            path = os.path.join(os.path.dirname(__file__), '../html/details.html')
            shared.render(self, path, template_values)
            
    
    def post(self):
        media=self.getMedia(self.request.get('key'))
        if media:
            comment=Comment()
            comment.title=self.request.get('title')
            u=users.get_current_user()
            if u:
                comment.by=u.nickname()
            else:
                comment.by="Mr. I'm too good to log in"
            comment.text=self.request.get('text')
            commentkey=self.request.get('commentkey')
            if commentkey:
                comment.op=Comment.get(commentkey)
            else:
                comment.media=media
            comment.put()
                
            template_values = {"media":media}
            path = os.path.join(os.path.dirname(__file__), '../html/details.html')
            shared.render(self, path, template_values)
        
    def getMedia(self, key):
        if key:
            return Media.get(key)
        else:
            shared.do404(self)