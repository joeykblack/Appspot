'''
Create on Jul 1, 2010
@author auser
'''

from google.appengine.ext.db import djangoforms
from model.comic import Comic
from django import newforms

class ComicForm(djangoforms.ModelForm):
    
    text=newforms.CharField(widget=newforms.Textarea(attrs={'rows':3,'cols':40}))
 
    class Meta:
        model = Comic
        exclude = ['last','owner']