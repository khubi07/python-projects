import random

#roll func
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value , max_value)
    return roll


#entry of players
while True:
    player = input("enter no. of players(1-4): ")
    if player.isdigit():
        player = int(player)
        if 1 < player <= 4:
            break
        else:
            print("must be btn 2-4")
    else:
        print("invalid input")


max_score = 50

#list stores all the playes's score
player_score = [0 for _ in range(player)] 
print(player_score)


#turn stimulation
while max(player_score) <= max_score: #ensures loops run tillwe get winner


    #ensure turns of player 
    for player_idx in range(player):
            print("\nplayer",player_idx + 1 ," turn has just started ")
            print('your total score is:', player_score[player_idx],"\n")
            current_score =0

            #while true means jab tak sare player ki turn nhi ho jati tab tk loop on
            while True:
                #everytime they'll b asked to play or not
                #if ans is other than yes loop breaks and next player turn comes
                should_roll = input("would u like to roll a die(y)? ")
                if should_roll.lower() != "y":
                    break
                
                value = roll()
                if value == 1:
                    print("you rolled 1, turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("you rolled:", value)
                print("you score: ", current_score)
            
            #temp score is added to actual score and displayed
            player_score[player_idx] += current_score
            print("your total score: ",player_score[player_idx])

#winner
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("\nplayer number", winning_idx+1, "is the winner with score: ",max_score)
