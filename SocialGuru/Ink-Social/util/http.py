'''
Created on May 29, 2012

@author: joey
'''
import urllib2


def getHttp(url):
    page=""
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0'), ('HOST',None)]
    filehandle = opener.open(url)
    for line in filehandle.readlines():
        page+=line
    filehandle.close()
    return page
    