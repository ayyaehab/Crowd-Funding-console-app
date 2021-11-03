
def P_create(x):
    mail = x
    title= input("enter ptoject name :")
    Details= input("enter ptoject Details:")
    target= input("enter ptoject target:")
    newpro = ",".join([title,Details,target,mail])
    newpro=newpro+"\n"
    projects=open("projects.txt","a")
    projects.write(newpro)
    projects.close()
def P_view():
    f = open("projects.txt", "r")
    print(f.read())
def P_delete(x):
    mail = x 
    # print (mail)
    dname= input("enter ptoject name you want to delete:")
    f = open("projects.txt", "r")
    projects =[]
    for n in f:
        projects.append(n.strip("\n"))
    print( "before: ",projects)
    for y in projects:
        item=y.split(",") 
        if dname==item[0] and mail==item[3]:
            print(item[0],"founded")
            # projects.pop(0)
            projects.remove(y)
            newp = open("projects.txt", "w")
            for i in projects:
             newp.write(i+"\n")
            newp.close()
            print("after: ", projects)
            return
    print(" not found")
    print("after: ", projects)
    # P_view()
 #///////////////////////////////////////////////////
def P_update(x):
    mail = x  
    dname= input("enter ptoject name you want to update:")
    f = open("projects.txt", "r")
    projects =[]
    for n in f:
      projects.append(n.strip("\n"))
    print( "before update: ",projects)
    for y in projects:
        project=y.split(",")
        if dname==project[0] and mail==project[3]:
            print("founded")
            m=projects.index(y) 
            project[0]= input("update ptoject name :")
            project[1]= input("edit ptoject Details:")
            project[2]= input("enter ptoject target:")
            y=",".join(project)
            projects[m]=y
            newp = open("projects.txt", "w")
            for i in projects:
             newp.write(i+"\n")
            newp.close()
            print(project)
            print(y)
            print("after update: ", projects)
            return
    print(" not found") 
    #///////////////////////////////////////////////////
def project(x):
 while True:
    choice = input("plz write c for create ,v for view , e for edit , d for delete ")
    choice = choice.strip()
    if choice.isalpha():
        if choice=='c':
           P_create(x)
        elif choice=='v':
           P_view()
        elif choice=='e':
            P_update(x)
        elif choice=='d':
            P_delete(x)
            break  
