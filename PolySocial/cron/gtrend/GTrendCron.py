'''
Created on May 29, 2012

@author: joey
'''
from cron.gtrend.scraper import HotTrendsScraper
from util import http
import logging
from util.BeautifulSoup import BeautifulSoup
from model.story import Story
from util.BeautifulSoup import Tag

def doCron(stories):
    raw_data = http.getHttp("http://www.google.com/trends/hottrends?sa=X")
    scraper=HotTrendsScraper()
    scraper.feed(raw_data)
    data = scraper.trends
    for d in data:
        buildStoryFromString(d, stories)
        

def findStory(data, stories):
    for story in stories:
        if story.mykey==data:
            return story
    return None


def buildStoryFromString(data, stories):
    story=findStory(data, stories)
    if not story:
        url="http://www.google.com/search?q="+data.replace(' ', '+')
        logging.info(url)
        try:
            raw_data = http.getHttp(url)
            soup = BeautifulSoup(raw_data)
            story=None
            a=soup.find(lambda tag: tag.name=='a' and tag.attrs[0][0]=='href' and not tag.attrs[0][1].startswith('/') and not 'google' in tag.attrs[0][1])
            if a and a.text:
                story=Story()
                story.deleteFlag=False
                story.mykey=data
                story.title=''
                for c in a.contents:
                    if type(c) == Tag:
                        story.title+=c.text
                    else:
                        story.title+=c
                story.link=a.attrs[0][1]
                story.text=''
                for c in a.parent.contents[4].contents:
                    if type(c) == Tag:
                        story.text+=c.text
                    else:
                        story.text+=c
                story.put()
        except DownloadError: #@UndefinedVariable
            logging.error(url + ' failed to load')
    
    '''
    scraper=SearchScraper()
    scraper.feed(raw_data)
    return scraper.story
    '''
    
    
    
    
    