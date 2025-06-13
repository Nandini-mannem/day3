def person(logined,user):
    if(logined==True):
        if(user=="admin"):
            return "welcome admin"
        else:
            return "welcome user"
    else:
         return "go and login first"
print(person(True,"user"))
  