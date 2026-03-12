from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)'''



def load_key():
   file = open('key.key','rb')
   key1 = file.read()
   file.close()
   return key1


master_password = input("What is your master password : ")
key = load_key() + master_password.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f:
            name, password = line.strip().split("|")
            print("User:", name, "| Password:", fer.decrypt(password.encode()).decode())

def add ():
    name = input("What is your username? ")
    password = input("Key in your password :")

    with open('passwords.txt','a') as f:
        f.write(name + "|" +  fer.encrypt(password.encode()).decode() +"\n")
    

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