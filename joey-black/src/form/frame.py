'''
Create on Jun 3, 2010
@author joeykblack
'''

from google.appengine.ext.db import djangoforms
from model.comic import Frame
from django import newforms

class FrameForm(djangoforms.ModelForm):
    
    text=newforms.CharField(widget=newforms.Textarea(attrs={'rows':3,'cols':40}))
    
    class Meta:
        model = Frame
        exclude = ['img','last','owner','comic','frameseq']