import random
temp = 0
print("\nWelcome to ROCK PAPER SCISSOR GAME\nIt's YOU V/S AI")
UserName = input("\nPlease Enter your name PLAYER:")
UserWish = 1
AIScore = UserScore = 0
while(temp == 0):
    match UserWish:
        case 1:
            print("\nEnter 1 to play ROCK!\nEnter 2 to play PAPER!\nEnter 3 to play SCISSOR!")
            UserInput = int(input("Please make a choice:"))
            AIChoice = random.randint(1,3)
            if(UserInput>3 or UserInput<1):
                print("\nInvalid Input You LOST THE ROUND!!!!!!!!")
            elif(UserInput == AIChoice):
                print(f"\nAI chose {AIChoice}")
                print("It's a TIE!!!!!!!")
            elif(UserInput == 1 and AIChoice == 3):
                print(f"\nAI chose {AIChoice}")
                print(f"Congratulations {UserName} you WON the Round!!!")
                UserScore = UserScore + 1
            elif(UserInput == 2 and AIChoice == 1):
                print(f"\nAI chose {AIChoice}")
                print(f"Congratulations {UserName} you WON the Round!!!")
                UserScore = UserScore + 1
            elif(UserInput == 3 and AIChoice == 2):
                print(f"\nAI chose {AIChoice}")
                print(f"Congratulations {UserName} you WON the Round!!!")
                UserScore = UserScore + 1
            else:
                print(f"\nAI chose {AIChoice}")
                print(f"You Lost Better Luck Next Round!!!")
                AIScore  = AIScore + 1
        case 2:
            temp = 1
            break
    print("\nEnter 1 to PLAY NEXT ROUND\nEnter 2 to EXIT")
    UserWish = int(input("Please make a WISH:"))        
with open("python/ROCK PAPER SCISSOR/score.txt") as f:
    Hscore = list(f.read())
    Hscore = int(Hscore[0])
    print(f"\nHigestscore is {Hscore}")
if(Hscore < (UserScore - AIScore)):
    with open("python/ROCK PAPER SCISSOR/score.txt", "w") as a:
        a.write(f"{UserScore - AIScore}")
print(f"Your Total score:{UserScore - AIScore}") if UserScore > AIScore else print("Your Total score:0")