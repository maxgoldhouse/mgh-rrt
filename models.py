from google.appengine.ext import ndb

class mghrrt(ndb.Model):
  whohash = ndb.StringProperty()
  what = ndb.StringProperty()
  when = ndb.DateTimeProperty(auto_now_add=True)
  
class mghwhohash(ndb.Model):
    whohash = ndb.StringProperty()
    who = ndb.StringProperty()
    when = ndb.DateTimeProperty(auto_now_add=True)