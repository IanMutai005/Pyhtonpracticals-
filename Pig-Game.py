import random

def roll():
    max_number = 1
    min_number = 6
    roll = random.randint(max_number,min_number)
    return roll

while True :

    players = input("Enter the number of players : ")

    if players.isdigit():
        players = int(players)
        break

    else :
        print("Wrong input ")
        continue

player_scores = [0 for _ in range(players)]

max_score = 20
current_score = 0

while max_score >  max(player_scores) :
    for player_idx in range(players):
        print("The turn of player number ", player_idx + 1 , " has begun")
      
        while True :
            answer = input("Would you like to roll the dice (y/n) : ").lower()
            if answer == "y" :
                value = roll()
                print("You rolled a ",value)

                if value != 1  :
                    current_score += value
                    
                
                else :
                    print("Unlucky mate ! no score on this round")

                break
            elif answer == "n":
                quit()
            else :
                print("Invalid input , please try again ")
                continue
        
        
        player_scores [player_idx] = current_score

highest_score = max(player_scores)
winning_index = player_scores.index(highest_score)

print("The players scored the following : ", player_scores ) 
print("Highest score being : ", highest_score)
print("Winning index being : ", winning_index)