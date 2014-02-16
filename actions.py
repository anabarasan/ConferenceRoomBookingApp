from google.appengine.ext.ndb import Key
from models import conferencerooms, schedule

# import logging

class ConferenceRoomSchedule:
    def __init__(self, kwargs):
        self.args = kwargs
#         self.skejule = getModel('schedule', kwargs)
        Id = kwargs.get('id', None)
        if (Id == None) or (len(Id.strip()) == 0):
            self.skejule = schedule()
        else:
            self.skejule = Key("schedule" ,int(Id)).get()

    def create(self):
        skejule = self.skejule
        skejule.room         =  self.args['room']
        skejule.blockedfrom  =  self.args['from']
        skejule.blockedto    =  self.args['to']
        skejule.blockedby    =  self.args['by']
        skejule.status       =  "blocked"
        skejule.put()
        return {'id' : str(self.skejule.key.id())}
        
    def list(self):
        return self.skejule.query()
      
    def update(self):
        skejule = self.skejule
        skejule.room         =  self.args['room']
        skejule.blockedfrom  =  self.args['from']
        skejule.blockedto    =  self.args['to']
        skejule.blockedby    =  self.args['by']
        skejule.status       =  self.args['status']
        skejule.put()
      
    def delete(self):
        self.skejule.key.delete()
        
    def getSkejule(self):
        return self.skejule

class ConferenceRoom:
    def __init__(self, kwargs):
        self.args = kwargs
#         self.room = getModel('conferencerooms', kwargs)
        Id = kwargs.get('id', None)
        if (Id == None) or (len(Id.strip()) == 0):
            self.room = conferencerooms()
        else:
            self.room = Key("conferencerooms", int(Id)).get()
        
    def create(self):
        room = self.args.get('room', None)
        if (room != None) or (len(room.strip()) > 0):
            self.room.room = room
            self.room.put()
            return {'id' : str(self.room.key.id())}
        else:
            return {'error' : 'room name cannot be null / empty'}
    
    def list(self):
        return self.room.query()
    
    def update(self):
        self.room.room = self.args.get('roomname', self.room.room)
        self.room.put()
         
    def delete(self):
        self.room.key.delete()
        
def getModel(model, args):
    Id = args.get('id', None)
    if (Id == None) or (len(Id.strip()) == 0):
        return getattr(model, "__init__")
    else:
        return Key(model,int(Id)).get()