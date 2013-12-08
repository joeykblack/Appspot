'''
Created on Jun 11, 2012

@author: joey
'''
from google.appengine.ext import webapp
from util import http

class OpenClipart(webapp.RequestHandler):
    
    def get(self):
        query=self.request.get('query')
        url='http://openclipart.org/api/search/?query='+query
        page=http.getHttp(url);
        self.response.out.write(page);