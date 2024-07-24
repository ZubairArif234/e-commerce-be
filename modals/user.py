import mongoengine as me
import datetime

class User(me.Document):
    username = me.StringField(required = True)
    email = me.StringField(required = True)
    password = me.StringField(required =True)
    # created_at = me.DateTimeField(default='klk')