"""
REST URLs for Booking
Create  /room/create/roomname
Read    /room/list
Update  /room/udpate/bookingid      params : roomname
Delete  /room/delete/bookingid
Create  /schedule/create            params : room, from, to, by
Read    /schedule/list
Update  /schedule/udpate/bookingid  params : room, from, to, by
Delete  /schedule/delete/bookingid
"""

import json, logging, webapp2
from actions import ConferenceRoom, ConferenceRoomSchedule
from Util import errorhandling

# map = {'schedule' : 'ConferenceRoomSchedule', 'room' : 'ConferenceRoom'}

class ScheduleHandler(webapp2.RequestHandler):
    def get(self, action):
        if action == 'list':
            logging.info(len(self.request.get("filter")))
            itenary = ConferenceRoomSchedule({}).list()
            out = []
            for schedule in itenary:
                skejule = {}
                skejule['id'] = str(schedule.key.id())
                skejule['room'] = schedule.room
                skejule['from'] = schedule.blockedfrom
                skejule['to'] = schedule.blockedto
                skejule['by'] = schedule.blockedby
                out.append(skejule)
            self.response.headers['Content-Type'] = "application/json"
            self.response.out.write({"schedule" : out})
        else:
            errorhandling(action, self.response)

    def post(self, action):
        if action == "create":
            data = json.loads(self.request.body)
            result = ConferenceRoomSchedule(data).create()
            self.response.headers['Content-Type'] = "application/json"
            self.response.out.write(result)
        else:
            errorhandling(action, self.response)
        
    def put(self):
        pass
        
    def delete(self):
        pass
    
class RoomHandler(webapp2.RequestHandler):
    def get(self, action):
        if action == 'list':
            rooms = ConferenceRoom({}).list()
            out = []
            for room in rooms:
                obj={}
                obj['id']= str(room.key.id())
                obj['room'] = room.room   
                out.append(obj)
            self.response.headers['Content-Type'] = "application/json"
            self.response.out.write({'rooms' : out} )
        else:
            errorhandling(action, self.response)
    
    def post(self, action, roomname):
        if action == 'create':
            result = ConferenceRoom({'room':roomname}).create()
            self.response.headers['Content-Type'] = "application/json"
            self.response.out.write(result)
        else:
            errorhandling(action, self.response)
        
    def put(self, action, roomid):
        if action == 'update':
            data = json.loads(self.request.body)
            roomname = data['roomname']
            ConferenceRoom({'id' : roomid, 'roomname' : roomname}).update()
        else:
            errorhandling(action, self.response)
        
    def delete(self, action, roomid):
        if action == 'delete':
            ConferenceRoom({'id':roomid}).delete()
        else:
            errorhandling(action, self.response)
      
class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass
    
app = webapp2.WSGIApplication([
    ('/schedule/(.*)/(.*)', ScheduleHandler),
    ('/schedule/(.*)', ScheduleHandler),
    ('/room/(.*)/(.*)', RoomHandler),
    ('/room/(.*)', RoomHandler),
    ('/', MainHandler)
], debug=True)
