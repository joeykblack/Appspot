'''
Created on Jun 22, 2010
@author auser
'''

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import images
from google.appengine.api.images import Image
from util import util
from model import comic
from form.frame import FrameForm
from action import frame
from form.comic import ComicForm

class Comic(webapp.RequestHandler):
    def get(self):
        
        comickey=self.request.get('comickey')
        c=None
        
        #get desired comic
        if comickey:
            c=comic.Comic.get(comickey)
            
            #delete
            type=self.request.get('type')
            if c and type and type=='delete':
                old=c
                for frame in old.frames:
                    frame.delete()
                if len(c.nexts.fetch(1))>0:
                    c=c.nexts.fetch(1)[0]
                else:
                    c=c.last
                for next in old.nexts.fetch(100):
                    next.last=old.last
                    next.put()
                old.delete()
        
        #move
        go=self.request.get('go')
        if go:
            if go=='last' and c and c.last:
                c=c.last
            elif go=='next' and c and len(c.nexts.fetch(1))>0:
                c=c.nexts.fetch(1)[0]
        
        #not found, get first
        if not c and len(comic.Comic.all().fetch(1))>0:
            c=comic.Comic.all().order('-date').fetch(1)
            if len(c)>0:
                c=c[0]
        
        #none found, make new
        if not c:
            c=comic.Comic(name="First", owner=users.get_current_user())
            c.put()
                
        
        template_values={}
        template_values.update(loadComicStd(c, self))

        template_values.update(util.loadstd(self))
        path = os.path.join(os.path.dirname(__file__), '../html/comicmain.html')
        self.response.out.write(template.render(path, template_values))
    
    def post(self):
        
        do=self.request.get('do')
        c=None
        rframeseq=None
        if do=="addcomic":
            c=newComic(self)
        elif do=="editcomic":
            c=editComic(self)
        else:
            rframeseq=saveFrame(self)
        
        if not c:
            comickey=self.request.get('comickey')
            c=comic.Comic.get(comickey)
            
        template_values={}
        template_values.update(loadComicStd(c, self))
        
        if rframeseq:
            template_values.update({'rframeseq':rframeseq})
        
        template_values.update(util.loadstd(self))
        path = os.path.join(os.path.dirname(__file__), '../html/comicmain.html')
        self.response.out.write(template.render(path, template_values))

def loadComicStd(c, handler):
    rframeseq=handler.request.get('rframeseq')
        
    template_values = {
                       'comic':c,
                       'rframeseq':rframeseq if rframeseq else getRightFrame(c),
                       'frameform':FrameForm(),
                       'isadmin':users.is_current_user_admin(),
                       'comicform':ComicForm(),
                       'comicnav':comicNav()
        }
    return template_values

def comicNav():
    comics=comic.Comic.all().order('-date').fetch(100)
    first=comics[-1]
    last=comics[0]
    comicnav='<a href=/comic?comickey='+str(first.key())+'>First Comic</a>...<a href=/comic?comickey='+str(last.key())+'>Newest Comic</a>'
    return comicnav
        
def getRightFrame(c):
    max=1
    for f in c.frames:
        if len(f.frameseq)>max:
            max=len(f.frameseq)
    if max>=5:
        return '1x1x1'
    elif max>=3:
        return '1x1'
    return '1'


def editComic(handler):
    edited=ComicForm(handler.request.POST).save(commit=False)
    
    edited.text=edited.text.replace('\n', '<br />')
    
    thisc=comic.Comic.get(handler.request.get('comickey'))
    
    thisc.name=edited.name
    thisc.text=edited.text
    thisc.tip=edited.tip
    
    thisc.put()
    
    return thisc
        
def newComic(handler):
    nextc=ComicForm(handler.request.POST).save(commit=False)
    
    nextc.text=nextc.text.replace('\n', '<br />')
    
    lastc=comic.Comic.get(handler.request.get('comickey'))
    
    nextc.last=lastc
    nextc.put()
    
    return nextc
        
def saveFrame(handler):
    newframe=FrameForm(handler.request.POST).save(commit=False)
    
    comickey=handler.request.get('comickey')
    
    # image
    img=handler.request.get('img')
    if img:
        newframe.img=db.Blob(getScaledImage(img))
    
    newframe.owner=users.get_current_user()
    newframe.comic=comic.Comic.get(comickey)
    
    #newframe seq
    rframeseq=handler.request.get('rframeseq')
    if not rframeseq or not newframe.comic.frames:
        newframe.frameseq='1'
    else:
        newframe.frameseq=rframeseq
        
    #remove old frame
    oldframe=frame.getFrame(key=comickey, rframeseq=newframe.frameseq)
    if oldframe:
        oldframe.delete()
    
    newframe.put()
    return newframe.frameseq
    
#find the last existing frame to create kid under
def getLastFrame(frameseq, mycomic):
    lastframeseq=frame.backFrameSeq(frameseq)
    if not lastframeseq or lastframeseq=='':
        return 0
    lastframe=0
    for f in mycomic.frames:
        if lastframeseq==f.frameseq:
            lastframe=f
            break
    if lastframe:
        return lastframe
    else:
        return getLastFrame(lastframeseq, mycomic)
    
    
    
def getScaledImage(image):
    width=290
    height=290
    return images.resize(image, width, height, images.PNG)
