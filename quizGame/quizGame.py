print("Welcome to my computer quiz")
playing = input("do you want to play ? ").lower()

if playing != "yes":
    print("have a good day!")
    quit()
    
print("let's start")
score = 0

ans = input("who is the founder of facebook? ")
if ans.lower() == "Mark zuckerberg": #capitalize ans of usr so it dont get wrong
    print("correct!")
    score += 1
else:
    print("wrong!")
    score -= 1

ans = input("Longest river in the world? ")
if ans.lower()  == "nile": #capitalize ans of usr so it dont get wrong
    print("correct!")
    score += 1
else:
    print("wrong!")
    score -= 1

ans = input("largets ocean by surface area? ")
if ans.lower()  == "pacific ocean": #capitalize ans of usr so it dont get wrong
    print("correct!")
    score += 1
else:
    print("wrong!")
    score -= 1

ans = input("capital of australia ? ")
if ans.casefold() == "canberra": #capitalize ans of usr so it dont get wrong
    print("correct!")
    score += 1
else:
    print("wrong!")
    score -= 1

ans = input("writer of Romeo and Juliet? ")
if ans.casefold() == "william shakespeare": #capitalize ans of usr so it dont get wrong
    print("correct!")
    score += 1
else:
    print("wrong!")
    score -= 1

ans = input("red planet? ")
if ans.casefold()== "mars": #capitalize ans of usr so it dont get wrong
    print("correct!")
    score += 1
else:
    print("wrong!")
    score -= 1

print("your score : ",score)