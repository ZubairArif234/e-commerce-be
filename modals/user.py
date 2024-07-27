import mongoengine as me


class User(me.Document):
   
    firstName = me.StringField(required = True)
    lastName = me.StringField(required = True)
    email = me.StringField(required = True  )
    password = me.StringField(required =True)
    role = me.StringField(default="user")
    verificationOtp = me.IntField()  
    otpExpiration = me.DateTimeField()
    isActive = me.BooleanField(default=False)
    emailVerified = me.BooleanField(default=False)
    
    def userDetail(self):
        return{
            "_id":str(self.id),
            "firstName":self.firstName,
            "lastName":self.lastName,
            "email":self.email,
            "role":self.role
        }