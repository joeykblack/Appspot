'''
Created on Jun 1, 2012

@author: joey
'''

import tweepy

def tweet(msg):
    CONSUMER_KEY = 'zQr7I8340V6hnz4F475vOA' 
    CONSUMER_SECRET = 'aMSfNoyQn5dehQPsV6tam0A62Kd6Q959e0PAB9KzRs'
    
    # for PolySocial1
    ACCESS_KEY = '596452693-kldKSMD1KJDfmWMQ7kd0ZS6b9U6xfFdixl1g6y0Y'
    ACCESS_SECRET = 'nJQqK45HGt9t2tep5J2TdOn0Iz5JWfbs5gGPTN0JOs'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(msg)