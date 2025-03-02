name = input("enter your name : ")
print(f"hello {name} welcome to game")
ans = input("do you want to play?(yes/no): ").lower()


while (ans=="yes"):
    ans = input("you are on the end of dirt road. Choose L/R : ").lower()
    if ans == "l":
        q1 = input("river around, do you wish to walk around/swim accros(swim/walk) : ").lower()

        if q1 == "swim":
            print("oops! you got eaten by aligator")
        elif q1 == "walk":
            print("oops! you died as you ran out of water")
        else:
            print("wrong option , you lose")
            break

    elif ans == "r":
        q2 = input("there's a bridge, wanna cross or head back?(y/n): ").lower()

        if q2 == "n":
            print("you go back and lose")
        elif q2 == "y":
            q3 = input("you cross the bridge and met a stranger. wanna talk?(y/n)").lower()

            if q3 == "y":
                print("he gave you gold and you won")
            else:
                print("you lost since you ignored the stranger. he was about to giv you gold")

        else:
            print("wrong option,you lose")
            break

    else:
        print("wrong way , you lose")
        break


print("have a good day")