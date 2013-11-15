'''
Create on Jun 3, 2010
@author joeykblack
'''

from google.appengine.ext.db import djangoforms
from model.blog import Entry
from django import newforms

class EntryForm(djangoforms.ModelForm):
    
    text=newforms.CharField(widget=newforms.Textarea(attrs={'rows':20,'cols':100}))
    
    class Meta:
        model = Entry
        exclude = ['by', 'user', 'img', 'posted', 'cparent', 'votes']