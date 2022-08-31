import random
print("Welcome to Number guessing game!")
NoofPlayers=int(input("Please enter no. of players:"))#3
PlayersList=[]
for i in range(NoofPlayers):
    name=input("Enter player {0}:".format(i+1))
    PlayersList.append(name)

WinnersList=[]
Hints=False
for i in PlayersList:
    PlayerName=i
    print("Welcome {0}".format(i))
    PlayerReady=0
    PlayerReady=int(input("{} are you ready?. Enter 1 for ready: ".format(PlayerName)))
    print("You have 3 chances, All the best!")
    if (PlayerReady):
        RandomNumber=random.randint(0,10)
        Hints=int(input("You need hints?, Enter 1 for hints & 0 for no hints:"))
        for i in range(3):
            if Hints:
                GuessNum= int(input("Enter your {0} Guess Num: ".format(i+1)))
                if GuessNum==RandomNumber:
                    WinnersList.append(PlayerName)
                    print("You Won {0}!!....".format(PlayerName))
                    break
                elif GuessNum<RandomNumber:
                    print("You have entered lower num than expected")
                elif GuessNum>RandomNumber:
                    print("You have entered greater num than expected")   
            else:
                GuessNum= int(input("Enter your {0} Guess Num: ".format(i+1)))
                if GuessNum==RandomNumber:
                    WinnersList.append(PlayerName)
                    print("You Won {0}!!....".format(PlayerName))
                    break
                else:
                    continue#skip               
        else:
            print("You lost!!")
            print("Actuall Number is: ",RandomNumber)

print("Congracts to {0} Winners:".format(len(WinnersList)))
print(*WinnersList)