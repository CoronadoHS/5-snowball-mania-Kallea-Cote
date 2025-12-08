''' 
    Name: Snowball-Mania
    Author: Kallea Cote
    Date: 12/5/25
    Class: AP Computer Science Principles
    Python: 
'''

import random
import time


def printIntro():
    '''
    ' Param: none
    ' 
    ' Print a welcome message to the user
    ' 
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("❄️  Welcome to Snowball Mania!❄️")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def getNames():
    '''
    ' Param: none
    ' 
    ' Create a list to hold player names.
    ' Ask the user for their name.  Store it in a variable and add it to the player list.
    ' Print instructions for the user to add more players and to type "DONE" when finished.
    ' Read in the first additional player name.
    ' While the user hasn't typed "DONE", add the new name to the player list and prompt for the next name
    ' After the user is finished entering names, print a "Time to play!" message
    '
    ' Return: the list of player names
    ' 
    '''
    players = []
    thisname = input("What is your name?   ")
    players.append(thisname)
    print("Who do you want to play in a snowball fight (one at a time)? Type done when you are finished!   ")
    fname1= input()
    while (fname1 != "done"):
        players.append(fname1)
        fname1 = input()
    print("Time to Play!!!")
    return players
    


def getThrower(players):
    '''
    ' Param: players (list of player names)
    '
    ' Return a randomly chosen player name to be the next thrower.
    '
    ' Return: player name
    '''
    return random.choice(players)

    
def getVictim(players, t):
    '''
    ' Param: players (list of player names), t (the thrower for this round)
    ' 
    ' Select a random player to be the next victim.  
    ' While the victim is the same player as the thrower, randomly select a new victim from the list.
    ' Return the victim's name.
    '
    ' Return: victim's name
    '''
    v = random.choice(players)
    while v == t:
        v = random.choice(players)
    return v 


def getHitResult():
    '''
    ' Param: none
    ' 
    ' Generate a random number between 1 and 10
    ' If the number is greater than ___, return True
    ' Else, return False
    '
    ' Return: Boolean representing whether or not the snowball hit
    '''
    hit_Num = random.randint(1,10)
    if (hit_Num % 2 == 1):
        return True
    else:
        return False
    

def playSnowballFight(players):
    '''
    ' Param: players (a list of players still in the game)
    '
    ' While there are still multiple players in the game...
    '   - Get the next thrower
    '   - Get the next victim
    '   - Get the next hit result
    '   - If a hit occurred, flip a coin to see if it is a knockout or not.
    '     - If knockout, print a knockout message and remove the victim from the list
    '     - Else, print a hit message but do not remove victim
    '   - Else, print a miss message
    '   - time.sleep(3) - delay execution for three seconds
    ' 
    ' Return: none
    '''
    while (len(players) >= 2):
        thrower = getThrower(players)
        victim = getVictim(players, thrower)
        hitresult = getHitResult()
        if (hitresult == True):
            koresult = random.randint(1, 2)
            if koresult == 1:
                print(thrower + " nailed "+ victim + " - knockout!!! ")
                players.remove(victim)
            else:
                print(thrower + " throws and hits " + victim + " but they survives to fight another day! ")
        else:
            print (thrower + " throws at " + victim + " but missed! " )
        time.sleep(3)


    
def printOutro(winner):
    '''
    ' Param: name of the winner
    ' 
    ' Print a congratulatory message naming the winner
    '
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("All hail " + winner + ", the Ultimate Student/Snowball Wizard!")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def runProgram():
    '''
    ' Param: none
    ' 
    ' Call the method that will print the intro messages
    ' Call the method that will return a list of player names.  Save the list in a variable.
    ' Call the method that will simulate the snowball fight
    ' Call the method that will print the outro messagees
    '
    ' Return: none
    '''
    printIntro()
    playernames = getNames()
    playSnowballFight(playernames)
    printOutro(playernames[0])


runProgram()
