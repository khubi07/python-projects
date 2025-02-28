import random
print("Welcome To RPS")

#seting variables
user_win = 0
pc_win = 0
tie = 0
options = ["r","p","s"]

while True:
    #user ip
    user_ip = input("type R/P/S or Q to quit: ").lower()
    if user_ip == "q":
        break

    if user_ip not in options:
        continue
    
    #pc input
    random_num = random.randint(0,2)
    pc_pick = options[random_num]
    print("pc's choice : ",pc_pick)

    #check who wins
    if user_ip == "r" and pc_pick == "s":
        print("you won!")
        user_win += 1

    elif user_ip == "s" and pc_pick == "r":
        print("pc won!")
        pc_win += 1

    elif user_ip == "s" and pc_pick == "p":
        print("you won!")
        user_win += 1

    elif user_ip == "p" and pc_pick == "s":
        print("pc won!")
        pc_win += 1

    elif user_ip == "p" and pc_pick == "r":
        print("you won!")
        user_win += 1

    elif user_ip == "r" and pc_pick == "p":
        print("pc won!")
        pc_win += 1
    else:
        print("its a tie")
        tie += 1

print("you won ",user_win, "times")
print("pc won ",pc_win, "times")
print("No. of ties ",tie)
print("have a good day")