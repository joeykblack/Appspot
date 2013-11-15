'''
Created on Jun 3, 2010

@author: joeykblack@gmail.com
'''
import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from model.blog import Entry, Tag, TagedEntry
from form.blog import EntryForm
from google.appengine.ext import db
import model
from model.user import Minime

def loadstd(handler):
    css='<link rel="stylesheet" type="text/css" href="/css/jkb.css" />'
    menu=loadmenu()
    banner=loadbanner()
    loginout=loadloginout(handler)
    
    m={
       'css':css,
       'banner':banner,
       'menu':menu,
       'loginout':loginout
       }
    return m


def loadmenu():
    path = os.path.join(os.path.dirname(__file__), '../html/menu.html')
    return template.render(path, {})

def loadbanner():
    path = os.path.join(os.path.dirname(__file__), '../html/banner.html')
    return template.render(path, {})

def loadloginout(handler):
    user = users.get_current_user()
    loginout='<div class="loginout">'
    if user:
        loginout+=user.nickname()+' - '
        if users.is_current_user_admin():
            loginout+='<a href="/admin">Admin</a> | <a href="/post">Post</a> | '
        loginout+='<a href="'+users.create_logout_url(handler.request.uri)+'">Logout</a>'
    else:
        loginout+='Hi stranger - '
        loginout+='<a href="'+users.create_login_url(handler.request.uri)+'">Login</a>'
    loginout+='</div>'

    return loginout




def saveEntry(handler):
    # load form
    key=handler.request.get('editkey')
    if key:
        entry=Entry.get(key)
        entry=EntryForm(data=handler.request.POST, instance=entry).save(commit=False)
    else:
        entry=EntryForm(handler.request.POST).save(commit=False)
    
    # get user
    user=users.get_current_user()
    if user:
        entry.user=user
        localuser=Minime.all().filter('user = ', user).get()
        if not(localuser):
            localuser=Minime(user=user, votes=0)
            localuser.put()
    alias=handler.request.get('alias')
    if alias:
        entry.by=alias
    elif users.get_current_user():
        entry.by=users.get_current_user().nickname()
    else:
        entry.by='stranger'
    
    # image
    img=handler.request.get('img')
    if img:
        entry.img=db.Blob(img)
        
    # replace \n on text with <br /> but not on html entries
    if entry.type=='Text':
        entry.text=entry.text.replace('\n', '<br />')
        
    # set parent
    topkey=handler.request.get('topkey')
    if topkey:
        cparent=Entry.get(topkey)
        if cparent:
            entry.cparent=cparent
   
    # save
    entry.put()
          
    # tag (entry must be saved)
    tagnames=handler.request.get('tags')
    if tagnames:
        tagnames=tagnames.split(',')
        for tagname in tagnames:
            tag=Tag.all().filter('name = ', tagname).get()
            if tag:
                if model.blog.containsEntry(tag.tagedEntries, entry)==-1:
                    TagedEntry(tag=tag, entry=entry).put()
            elif not(tag):
                tag=Tag(name=tagname).put()
                TagedEntry(tag=tag, entry=entry).put()
                
    # removed tags
    if entry.tagedEntries:
        for tagedEntry in entry.tagedEntries:
            found=False
            if tagnames:
                for tagname in tagnames:
                    if tagedEntry.tag.name==tagname:
                        found=True
            if not(found):
                if len(tagedEntry.tag.tagedEntries.fetch(100))==1:
                    tagedEntry.tag.delete()
                tagedEntry.delete()


def imageafi(entries):
    for entry in entries:
        if entry.img:
            entry.text=imageafiText(entry)
    return entries

def imageafiText(entry):
    return entry.text.replace('(img)', '<img src="img?img_id=%s"></img>'%entry.key())


    
def filters(action):
    tags=Tag.all().fetch(100)
    result='<p>filter: <a href="/'+action+'">all</a>'
    for tag in tags:
        result+=' | <a href="/'+action+'?tag='+tag.name+'">'+tag.name+'</a>'
    result+='</p>'
    
    return result


def vote(handler):
    localuser=Minime.all().filter('user = ', users.get_current_user()).get()
    if not(localuser):
        Minime(user=users.get_current_user(), votes=0).put()
    elif localuser.votes>0:
        votekey=handler.request.get('votekey')
        if votekey:
            localuser.votes-=1
            localuser.put() 
            vote=handler.request.get('vote')
            entry=Entry.get(votekey)
            if entry:
                if not(entry.votes):
                    entry.votes=0
                if vote=='up':
                    entry.votes+=1
                else:
                    entry.votes-=1
                entry.put()
            
            
        