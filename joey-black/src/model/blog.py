'''
Created on Jun 3, 2010
@author: auser
'''

from google.appengine.ext import db


class Tag(db.Model):
    name=db.StringProperty()
    
    

class Entry(db.Model):
    title=db.StringProperty()
    text=db.TextProperty()
    type=db.StringProperty(default='Text', choices=['Text', 'HTML'])
    
    posted=db.DateTimeProperty(auto_now_add=1)
    by=db.StringProperty()
    user=db.UserProperty()
    
    img=db.BlobProperty()
    
    cparent=db.SelfReferenceProperty(collection_name='comments')
    
    votes=db.IntegerProperty()
    
    def __eq__(self, other):
        return (self.title==other.title) & (self.text==other.text)
    
class TagedEntry(db.Model):
    tag=db.ReferenceProperty(Tag, collection_name='tagedEntries')
    entry=db.ReferenceProperty(Entry, collection_name='tagedEntries')
    
def containsEntry(arrTagedEntries, entry):
    i=-1
    for index, tagedEntrie in enumerate(arrTagedEntries):
        if tagedEntrie.entry==entry:
            i=index
            break
    return i
    