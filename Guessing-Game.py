import random 

count = 0

upper_limit = int(input("Pick a number that will be your upper limit "))

random_number = random.randint(0,upper_limit)

while True:
    user_guess = int(input("Choose any number that lies between 0 and that number "))
    
    if user_guess > 0 :
       
       if user_guess != random_number :
        print("Please try again")
        count +=1
        continue
      
       else :
        print("You are correct ")
        count +=1
        break     
  
    else :
      continue

    
    

print("You made a totatl of ", count ," attempts")





