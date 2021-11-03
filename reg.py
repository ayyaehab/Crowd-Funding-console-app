def Registration():
    fname= input("enter your first name :")
    lname= input("enter your last name:")
    email= input("enter your email:")
    password= input("enter your password:")
    newstr = ",".join([fname,lname,email, password])
    newstr=newstr+"\n"
    users=open("users.txt","a")
    users.write(newstr)
    users.close()
   
