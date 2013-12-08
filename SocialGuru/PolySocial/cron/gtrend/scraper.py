'''
Created on May 29, 2012

@author: joey
'''
from HTMLParser import HTMLParser
from model.story import Story


class HotTrendsScraper(HTMLParser):
    
    def __init__(self):
        self.scrape=False
        self.trends=[]
        self.reset()
    
    def handle_starttag(self, tag, attrs):
        if tag=="a" and [item for item in attrs if "/trends/hottrends?q" in item[1]]: 
            self.scrape=True
        
    def handle_endtag(self, tag):
        self.scrape=False
        
    def handle_data(self, data):
        if self.scrape:
            self.trends.append(data)
    


class SearchScraper(HTMLParser):
    
    def __init__(self):
        self.scrapeTitle=False
        self.scrapeText=False
        self.story = Story()
        self.reset()
    
    def handle_starttag(self, tag, attrs):
        if tag=="a" and [item for item in attrs if "/url?q" in item[1]]:
            self.scrapeTitle=True
            self.story.link=attrs.get("href").split("?q=")[1]
        elif tag=="div" and [item for item in attrs if item[1]=="s"]: 
            self.scrapeText=True
        
    def handle_endtag(self, tag):
        if tag=="a":
            self.scrapeTitle=False
        elif tag=="div":
            self.scrapeText=False
        
    def handle_data(self, data):
        if self.scrapeTitle:
            self.story.title=data
        elif self.scrapeText:
            self.story.text=data
    
    