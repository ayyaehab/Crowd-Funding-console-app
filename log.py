

        #///////////////////////////////
import project_op
def Login():
  email=input("enter your email:")
  password=input("enter your password:")
  f = open("users.txt", "r")
  users =[]
  for x in f:
        users.append(x.strip("\n"))
  for y in users:
        user=y.split(",") 
        if email==user[2] and password==user[3]:
          print(user[0]," you log in success")
          project_op.project(email)
          return
  print(email," not found")
  