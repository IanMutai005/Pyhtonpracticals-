master_password = input("What is your master password : ")

def view():
      with open('passwords.txt','r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            name , password = data.split("|")
            print("User :", name ,"Password : ",password)
    
     
 
def add ():
    name = input("What is your username? ")
    password = input("Key in your password :")

    with open('passwords.txt','a') as f:
        f.write(name + "|" +  password +"\n")
    

while True:
     mode = input("What would you like to do (view, add or quit )? : ")
    
     if mode == "quit":
        break
     
     if mode == "view":
        view()
                                
     elif mode == "add":
        add()
    
     else :
        print("Invalid input , please try again :")
        continue

print("You have completed managing your passwords")