'''
Created on May 30, 2012

@author: joey
'''
from util import http
from util.BeautifulSoup import BeautifulSoup
from model.video import Video


def getTags(entry):
    tags=[]
    for tag in entry('category'):
        if tag.attrs[1][0]=='term' and 'http:' not in tag.attrs[1][1]:
            tags.append(tag.attrs[1][1]) 
    return tags

def getCategories(entry):
    categories=[]
    for category in entry('category'):
        if len(category.attrs)>2 and category.attrs[2][0]=='label':
            categories.append(category.attrs[2][1].replace('&', 'and')) 
    return categories


def getVideo(videos, mykey):
    for video in videos:
        if video.mykey==mykey:
            return video
    return None


def doCron(videos):
    raw_data = http.getHttp("https://gdata.youtube.com/feeds/api/standardfeeds/on_the_web")
    soup = BeautifulSoup(raw_data, selfClosingTags=['category'])
    entries=soup.findAll('entry')
    for entry in entries:
        if len(entry('title'))>0:
            mykey=entry('title')[0].text if len(entry('title'))>0 else None
            if mykey and not getVideo(videos, mykey):
                video=Video()
                video.title=entry('title')[0].text
                video.mykey=mykey
                video.text=entry('content')[0].text if len(entry('content'))>0 else ''
                links=entry(lambda tag: tag.name=='link' and tag.attrs[2][0]=='href' and '/watch?' in tag.attrs[2][1])
                if len(links)==0:
                    continue
                video.link=links[0].attrs[2][1]
                imgs=entry('media:thumbnail',  height="90", width="120")
                if len(imgs)==0:
                    continue
                video.img=imgs[0].attrs[0][1] 
                imgsBig=entry('media:thumbnail',  height='360', width='480')
                if len(imgsBig)==0:
                    continue
                video.imgBig=imgsBig[0].attrs[0][1]
                video.tags=getTags(entry)
                video.categories=getCategories(entry)
                video.save();