ConferenceRoomBookingApp
========================

REST URLs for Booking

Conference Room
---------------

Create  /room/create/roomname

Read    /room/list

Update  /room/udpate/bookingid      params : roomname

Delete  /room/delete/bookingid

Conference Room Schedule
------------------------


Create  /schedule/create            params : room, from, to, by

Read    /schedule/list

Update  /schedule/udpate/bookingid  params : room, from, to, by

Delete  /schedule/delete/bookingid
