'''
Created on Jun 1, 2012

@author: joey
'''

import logging
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app


class LogSenderHandler(InboundMailHandler):
    def receive(self, message):
        logging.info("Received a message from: " + message.sender)
        message.sender = "joeykblack@gmail.com"
        message.to = "joeykblack@gmail.com"
        message.send()


application = webapp.WSGIApplication([LogSenderHandler.mapping()], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()