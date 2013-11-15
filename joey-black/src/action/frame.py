'''
Created on Jun 24, 2010
@author auser
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from model import comic


class Frame(webapp.RequestHandler):
    def get(self):
        
        type=self.request.get('type')
        fnum=self.request.get('fnum')
        rframeseq=self.request.get('rframeseq')
        k=self.request.get('key')
        
        frame=getFrame(key=k, fnum=fnum, rframeseq=rframeseq)
        
        if frame:
            if type=='text':
                re=frame.text
                self.response.out.write(re)
            elif type=='imgsrc':
                if frame.img:
                    re='/frame?type=image&key='+k+'&fnum='+fnum+'&rframeseq='+rframeseq
                    self.response.out.write(re)
                else:
                    self.response.out.write('none')
            elif type=='image':
                if frame.img:
                    self.response.headers['Content-Type'] = "image/png"
                    self.response.out.write(frame.img)
                else:
                    self.error(404)
            elif type=='delete':
                deleteFrame(frame)
        else:
            #self.error(404)
            self.response.out.write('')
            

def deleteFrame(frame):
    #resequence
    """
    if frame.last:
        count=1
        for f in frame.last.kids:
            if f.frameseq!=frame.frameseq:
                l=len(f.frameseq)
                f.frameseq=f.frameseq[0:l-1]+str(count)
                f.put()
                count+=1
    elif frame.comic.frames:
        count=1
        for f in frame.comic.frames:
            if len(f.frameseq)==1 and f.frameseq!=frame.frameseq:
                l=len(f.frameseq)
                f.frameseq=str(count)
                f.put()
                count+=1
    """
    #delete
    frame.delete()

def backFrameSeq(frameseq):
    l=len(frameseq)
    if l>=3:
        frameseq=frameseq[0:l-2]
    elif l>1:
        frameseq=frameseq[0:1]
    else:
        frameseq=''
    return frameseq

def getFrameSeq(fnum, rframeseq):
    frameseq=rframeseq
    fnum=int(fnum)
    for i in range(fnum, 3):
        frameseq=backFrameSeq(frameseq)
    return frameseq


def getFrame(key=None, fnum=None, rframeseq=None):
    c=comic.Comic.get(key)
    if fnum:
        frameseq=getFrameSeq(fnum=fnum, rframeseq=rframeseq)
    else:
        frameseq=rframeseq
    """
    if c:
        for f in c.frames:
            if frameseq==f.frameseq:
                frame=f
                break
    """
    frame=None
    if c:
        frame=c.frames.filter('frameseq = ', frameseq).get()
    return frame
