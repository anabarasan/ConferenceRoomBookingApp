from google.appengine.ext import ndb

class conferencerooms(ndb.Model):
    room = ndb.StringProperty();
    
class schedule(ndb.Model):
    room        = ndb.StringProperty()
    status      = ndb.StringProperty()
    blockedfrom = ndb.IntegerProperty()
    blockedto   = ndb.IntegerProperty()
    blockedby   = ndb.StringProperty()
    blockedon   = ndb.DateTimeProperty(auto_now_add=True)