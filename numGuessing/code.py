import random
top_of_range = input("type a num :")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("enter num > 0")
        quit()
else:
    print("enter a num not char/string")
    quit()

random_num = random.randint(0 , top_of_range)
guesses = 0 

while True:
    guesses += 1
    user_guess = input("Make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)

       
    else:
        print("enter a num not char/string")
        continue
    if user_guess == random_num:
        print("you got it!")
        break
    
    elif user_guess > random_num:
            print("you were above the num")
    else:
            print("you were below the num")

print("you got it right in ",guesses, "guesses")