'''
Created on Jun 1, 2012

@author: joey
'''
#!/usr/bin/env python

import tweepy


CONSUMER_KEY = 'zQr7I8340V6hnz4F475vOA'
CONSUMER_SECRET = 'aMSfNoyQn5dehQPsV6tam0A62Kd6Q959e0PAB9KzRs'
ACCESS_KEY = '596452693-kldKSMD1KJDfmWMQ7kd0ZS6b9U6xfFdixl1g6y0Y'
ACCESS_SECRET = 'nJQqK45HGt9t2tep5J2TdOn0Iz5JWfbs5gGPTN0JOs'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret