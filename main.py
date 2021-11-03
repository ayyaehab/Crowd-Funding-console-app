import reg
import log
import project_op
while True:
    choice = input("plz write l for login , r tor registeration ")
    choice = choice.strip()
    if choice.isalpha():
        if choice=='r':
           reg.Registration()
        elif choice=='l':
            log.Login()
            break  
