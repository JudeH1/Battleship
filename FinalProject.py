#jude hoekstra
# i pledge that all this work is my own
# except the button which is heavily modified but based on the textbook


#all of this is initializing important variables and importing stuff

from graphics import *
import random

import time

letters = "abcdef"
numbers = "123456"

playerClicked = False

global enemyHits
enemyHits = 0

#these two lists are used later to prevent ships from wrapping around the board
leftEdgeNumbers = [0, 6, 12, 18, 24, 30]
rightEdgeNumbers  = [5, 11, 17, 23, 29, 35]






enemylistoflists = [ ]
enemybuttonList = [ ]
enemybuttonLists = [ ]

playerlistoflists = [ ]
playerbuttonList = [ ]
playerbuttonLists = [ ]

gameOver = False

directions = ["up", "down", "left", "right"]

previousGuesses = [ ]
playerpreviousGuesses = [ ]

win = GraphWin("Battleship", 400, 600)
win.setCoords(-200, -300, 200, 300)


#this is the button class, modified to be a circle instead of a rectangle, and with some added functionality (displaying hits and player ships)

class Button:


    def __init__(self, win, centerx, centery, radius):
        x,y = centerx, centery
        r = radius * 2 - 5
        self.win = win
        self.centerx = centerx
        self.centery = centery
        self.radius = radius
        self.xmax, self.xmin = x+r, x-r
        self.ymax, self.ymin = y+r, y-r
        self.circ = Circle(Point(centerx, centery), radius)
        self.circ.setFill('black')
        self.circ.draw(win)
        self.deactivate()

    def clicked(self, p): #determines whether the button has been clicked
        return self.active and self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax
        
    
    def hit(self): #registers a hit at the button's location
        placeHit = Circle(Point(self.centerx, self.centery), self.radius)
        placeHit.setFill('red')
        placeHit.draw(self.win)
    
    def miss(self): #registers a miss at the button's location
        placeMiss = Circle(Point(self.centerx, self.centery), self.radius)
        placeMiss.setFill('white')
        placeMiss.draw(self.win)

    def place(self, win): #places a player ship at the button's location
        placeCircle = Circle(Point(self.centerx, self.centery), self.radius)
        placeCircle.setFill('gray')
        placeCircle.draw(self.win)

    def activate(self): #sets button to active
        self.active = 1

    def deactivate(self): #sets button to inactive
        self.active = 0
        


        
    

def initialize (): # this function will draw the window and allow the player to input where their ships are placed at the beginning of the game
    
    
    opponentScreen = Rectangle(Point(-100, 225), Point(100, 20))
    opponentScreen.setOutline("blue")
    opponentScreen.setFill("blue")
    opponentScreen.draw(win)
    
    playerScreen = Rectangle(Point(-100, -225), Point(100, -20))
    playerScreen.setOutline("blue")
    playerScreen.setFill("blue")
    playerScreen.draw(win)

    #draws all the spots and the numbers/letters on the side/top
    
    initialXcoord = -80 
    initialYcoord = -200
    sidenumber = 0
    sideY = 200
    sideX = -80
    for i in range (6):
        numbertext = Text(Point(sideX, 240), numbers[sidenumber])
        numbertext.setFill("black")
        numbertext.draw(win)
        sideX = sideX + 32
        sidenumber = sidenumber + 1
    sidenumber = 0
    
    for i in range (6):
        lettertext = Text(Point(-120, sideY), letters[sidenumber])
        lettertext.setFill("black")
        lettertext.draw(win)
        sideY = sideY - 32
        sidenumber = sidenumber + 1
        for i in range(6):
            button = Button(win, initialXcoord, initialYcoord, 10)
            enemybuttonLists.append(button)
            initialXcoord = initialXcoord + 32
        initialXcoord = -80
        initialYcoord = initialYcoord + 32
        enemylistoflists.append(enemybuttonLists)
     
    #does the same thing for the bottom board
    initialXcoord = 80 
    initialYcoord = 200
    sidenumber = 0
    sideY = -40
    sideX = -80
    for i in range (6):
        numbertext = Text(Point(sideX, -240), numbers[sidenumber])
        numbertext.setFill("black")
        numbertext.draw(win)
        sideX = sideX + 32
        sidenumber = sidenumber + 1
    sidenumber = 0
    for i in range (6):
        lettertext = Text(Point(-120, sideY), letters[sidenumber])
        lettertext.setFill("black")
        lettertext.draw(win)
        sideY = sideY - 32
        sidenumber = sidenumber + 1
        for i in range(6):
            button = Button(win, initialXcoord, initialYcoord, 10)
            playerbuttonLists.append(button)
            initialXcoord = initialXcoord - 32
        initialXcoord = 80
        initialYcoord = initialYcoord - 32
        playerlistoflists.append(playerbuttonLists)

    shiplength = 2
    
    
    
    # This huge block of code lets the player input their ships
    
   
    
    playerClicked = False
    shiplength = -1
    uporside = " "
    
    for i in range (3):
        
        shiplength = shiplength + 1
        
        
        
        for i in enemylistoflists:
            for j in i:
                if j not in playerbuttonList:
                    j.activate()
    
    #deactivates all the coordinates/buttons
                    
        for i in enemylistoflists:
            for j in i:
                if j in playerbuttonList:
                    j.deactivate()
    
        playerClicked = False   
    
        print("Click on the start point of the ship that is", shiplength + 2, "long")
    
        shiporigin = win.getMouse()
    
    #checks to see if the player has clicked on a button, if they have, places a gray circle there, deactivates the button, and adds it to a list of player buttons
        while playerClicked == False:
                for i in enemylistoflists:
                    for j in i:
                        if j.clicked(shiporigin) == True:
                            referenceSpot = i.index(j)
                            j.deactivate()
                            j.place(win)
                            playerbuttonList.append(j)
                            playerClicked = not playerClicked
                if playerClicked == False:           
                    print ("invalid point")
                    shiporigin = win.getMouse()
                else:
                    break
      #  print (referenceSpot)
        
        for i in enemylistoflists:
                for j in i:
                    j.deactivate()
    
    #finds what coordinates are next to the point/button/coordinate, activates them, thus making sure that the player can only choose coordinates next to the previous one
        #print (referenceSpot)
        for i in enemylistoflists:
            for j in i:
                secondSpot = i.index(j)
            
                if referenceSpot in leftEdgeNumbers: #checks to seeif the point is on the edge to prevent ships from wrapping around to a coordinate above them
                    if (secondSpot == (referenceSpot + 1)) and j not in playerbuttonList:
                        j.activate()
                    elif (secondSpot == (referenceSpot - 6) or secondSpot == (referenceSpot + 6)) and j not in playerbuttonList:
                        j.activate()
                elif referenceSpot in rightEdgeNumbers:
                    if (secondSpot == (referenceSpot - 1)) and j not in playerbuttonList:
                        j.activate()
                    elif (secondSpot == (referenceSpot - 6) or secondSpot == (referenceSpot + 6)) and j not in playerbuttonList:
                        j.activate()
                else:
                    if (secondSpot == (referenceSpot - 1) or secondSpot == (referenceSpot + 1)) and j not in playerbuttonList:
                        j.activate()
                    elif (secondSpot == (referenceSpot - 6) or secondSpot == (referenceSpot + 6)) and j not in playerbuttonList:
                        j.activate()
    
        print("Click on the next point of the ship")
    
        playerClicked = False
    
        shiporigin = win.getMouse()
    
        while playerClicked == False:
                for i in enemylistoflists:
                    for j in i:
                        if j.clicked(shiporigin) == True:
                            secondSpot = i.index(j)
                            j.deactivate()
                            j.place(win)
                            playerbuttonList.append(j)
                            playerClicked = not playerClicked
                if playerClicked == False:           
                    print ("invalid point")
                    shiporigin = win.getMouse()
                else:
                    break
        
        #records whether the ship is going up and down or side to side
        
        if (secondSpot == (referenceSpot - 1)) or (secondSpot == (referenceSpot + 1)):
            uporside = "side"
        elif (secondSpot == (referenceSpot - 6)) or (secondSpot == (referenceSpot + 6)):
            uporside = "up"
        
        
        thirdSpot = 10000000
        
        if shiplength > 0:
            for i in range (shiplength):
                for i in enemylistoflists:
                    for j in i:
                        j.deactivate()
        
        #makes coordinates available based on whether the ship is going up and down or side to side, and on what's adjacent to the previous coordinates
                for i in enemylistoflists:
                    for j in i:
                        nextSpot = i.index(j)
                        
                        if uporside == "side":
                            
                            if referenceSpot in leftEdgeNumbers:
                                if (nextSpot == (referenceSpot + 1)) and j not in playerbuttonList:
                                    j.activate()
                            if referenceSpot in rightEdgeNumbers:
                                if (nextSpot == (referenceSpot - 1)) and j not in playerbuttonList:
                                    j.activate()
                            if referenceSpot not in leftEdgeNumbers and referenceSpot not in rightEdgeNumbers:
                                if (nextSpot == (referenceSpot - 1) or nextSpot == (referenceSpot + 1)) and j not in playerbuttonList:
                                    j.activate()
                                    
                            if secondSpot in leftEdgeNumbers:
                                if (nextSpot == (secondSpot + 1)) and j not in playerbuttonList:
                                    j.activate()
                            if secondSpot in rightEdgeNumbers:
                                if (nextSpot == (secondSpot - 1)) and j not in playerbuttonList:
                                    j.activate()
                            if secondSpot not in leftEdgeNumbers and secondSpot not in rightEdgeNumbers:
                                if (nextSpot == (secondSpot - 1)) or (nextSpot == (secondSpot + 1)) and j not in playerbuttonList:
                                    j.activate()
                                    
                                    
                            if thirdSpot in leftEdgeNumbers:
                                if (nextSpot == (thirdSpot + 1)) and j not in playerbuttonList:
                                    j.activate()    
                            if thirdSpot in rightEdgeNumbers:
                                if (nextSpot == (thirdSpot - 1)) and j not in playerbuttonList:
                                    j.activate()
                            if thirdSpot not in leftEdgeNumbers and thirdSpot not in rightEdgeNumbers and (thirdSpot < 10000000) :
                                if (nextSpot == (thirdSpot - 1) or nextSpot == (thirdSpot + 1)) and j not in playerbuttonList:
                                    j.activate()
                            
                            
                        
                        else:
                            
                            if (nextSpot == (referenceSpot - 6) or nextSpot == (referenceSpot + 6)) and j not in playerbuttonList:
                                j.activate()
                            elif (nextSpot == (secondSpot - 6) or nextSpot == (secondSpot + 6)) and j not in playerbuttonList:
                                j.activate()
                            elif (nextSpot == (thirdSpot - 6) or nextSpot == (thirdSpot + 6)) and j not in playerbuttonList:
                                j.activate()
                                
            
                print("Click on the next point of the ship")
            
                playerClicked = False
    
                shiporigin = win.getMouse()
    
                while playerClicked == False:
                        for i in enemylistoflists:
                            for j in i:
                                if j.clicked(shiporigin) == True:
                                    thirdSpot = i.index(j)
                                    j.deactivate()
                                    j.place(win)
                                    playerbuttonList.append(j)
                                    playerClicked = not playerClicked
                                    
                                        
                        if playerClicked == False:           
                            print ("invalid point")
                            shiporigin = win.getMouse()
                        else:
                            break
                
    
        

def programInitialize (): #this function generates the program's initial ships, it's very inelegant and could be trimmed down a lot but when I tried to do so it didn't work so here we are
    
    #most of this code is the same as the player initialize, but there's some additional stuff to stop the program from generating invalid ships
    
    
    finished = False
    
    while finished == False:
        
        shipsPlaced = 0
        programFailed = False
        failedAttempts = 0
        playerClicked = False
        shiplength = -1
        uporside = " "
        
        for i in range (3):
            
            shiplength = shiplength + 1
            
            
            
            for i in playerlistoflists:
                for j in i:
                    if j not in enemybuttonList:
                        j.activate()
        
            for i in playerlistoflists:
                for j in i:
                    if j in enemybuttonList:
                        j.deactivate()
        
            playerClicked = False   
        
            
        
            shiporigin = Point(random.randint(-200, 200), random.randint(-300, 300))
        
            while playerClicked == False and j not in enemybuttonList:
                    for i in playerlistoflists:
                        for j in i:
                            if j.clicked(shiporigin) == True:
                                referenceSpot = i.index(j)
                                j.deactivate()
                                #j.place(win)                            
                                enemybuttonList.append(j)
                                playerClicked = not playerClicked
                    if playerClicked == False:
                        failedAttempts = failedAttempts + 1
                        if failedAttempts > 5000:
                            playerClicked = True
                        shiporigin = Point(random.randint(-200, 200), random.randint(-300, 300))
                    else:
                        break
          #  print (referenceSpot)
            
            for i in playerlistoflists:
                    for j in i:
                        j.deactivate()
        
            for i in playerlistoflists:
                for j in i:
                    secondSpot = i.index(j)
                
                    if referenceSpot in leftEdgeNumbers:
                        if (secondSpot == (referenceSpot + 1)) and j not in enemybuttonList:
                            j.activate()
                        elif (secondSpot == (referenceSpot - 6) or secondSpot == (referenceSpot + 6)) and j not in enemybuttonList:
                            j.activate()
                    elif referenceSpot in rightEdgeNumbers:
                        if (secondSpot == (referenceSpot - 1)) and j not in enemybuttonList:
                            j.activate()
                        elif (secondSpot == (referenceSpot - 6) or secondSpot == (referenceSpot + 6)) and j not in enemybuttonList:
                            j.activate()
                    else:
                        if (secondSpot == (referenceSpot - 1) or secondSpot == (referenceSpot + 1)) and j not in enemybuttonList:
                            j.activate()
                        elif (secondSpot == (referenceSpot - 6) or secondSpot == (referenceSpot + 6)) and j not in enemybuttonList:
                            j.activate()
        
            
        
            playerClicked = False
        
            shiporigin = Point(random.randint(-200, 200), random.randint(-300, 300))
        
            while playerClicked == False:
                    for i in playerlistoflists:
                        for j in i:
                            if j.clicked(shiporigin) == True and j not in enemybuttonList:
                                secondSpot = i.index(j)
                                j.deactivate()
                                #j.place(win)
                                enemybuttonList.append(j)
                                playerClicked = not playerClicked
                    if playerClicked == False:           
                        failedAttempts = failedAttempts + 1
                        if failedAttempts > 5000:
                            playerClicked = True
                        shiporigin = Point(random.randint(-200, 200), random.randint(-300, 300))
                    else:
                        break
            
            if (secondSpot == (referenceSpot - 1)) or (secondSpot == (referenceSpot + 1)):
                uporside = "side"
            elif (secondSpot == (referenceSpot - 6)) or (secondSpot == (referenceSpot + 6)):
                uporside = "up"
            
            thirdSpot = 10000000
            
            if shiplength > 0:
                for i in range (shiplength):
                    for i in playerlistoflists:
                        for j in i:
                            j.deactivate()
            
                    for i in playerlistoflists:
                        for j in i:
                            nextSpot = i.index(j)
                            
                            if uporside == "side":
                                if referenceSpot in leftEdgeNumbers:
                                    if (nextSpot == (referenceSpot + 1)) and j not in enemybuttonList:
                                        j.activate()
                                if referenceSpot in rightEdgeNumbers:
                                    if (nextSpot == (referenceSpot - 1)) and j not in enemybuttonList:
                                        j.activate()
                                if referenceSpot not in leftEdgeNumbers and referenceSpot not in rightEdgeNumbers:
                                    if (nextSpot == (referenceSpot - 1) or nextSpot == (referenceSpot + 1)) and j not in enemybuttonList:
                                        j.activate()
                                        
                                if secondSpot in leftEdgeNumbers:
                                    if (nextSpot == (secondSpot + 1)) and j not in enemybuttonList:
                                        j.activate()
                                if secondSpot in rightEdgeNumbers:
                                    if (nextSpot == (secondSpot - 1)) and j not in enemybuttonList:
                                        j.activate()
                                if secondSpot not in leftEdgeNumbers and secondSpot not in rightEdgeNumbers:
                                    if (nextSpot == (secondSpot - 1)) or (nextSpot == (secondSpot + 1)) and j not in enemybuttonList:
                                        j.activate()
                                        
                                        
                                if thirdSpot in leftEdgeNumbers:
                                    if (nextSpot == (thirdSpot + 1)) and j not in enemybuttonList:
                                        j.activate()    
                                if thirdSpot in rightEdgeNumbers:
                                    if (nextSpot == (thirdSpot - 1)) and j not in enemybuttonList:
                                        j.activate()
                                if thirdSpot not in leftEdgeNumbers and thirdSpot not in rightEdgeNumbers and (thirdSpot < 10000000) :
                                    if (nextSpot == (thirdSpot - 1) or nextSpot == (thirdSpot + 1)) and j not in enemybuttonList:
                                        j.activate()
                                    
                            
                            else:
                                if (nextSpot == (referenceSpot - 6) or nextSpot == (referenceSpot + 6)) and j not in enemybuttonList:
                                    j.activate()
                                elif (nextSpot == (secondSpot - 6) or nextSpot == (secondSpot + 6)) and j not in enemybuttonList:
                                    j.activate()
                                elif (nextSpot == (thirdSpot - 6) or nextSpot == (thirdSpot + 6)) and j not in enemybuttonList:
                                    j.activate()
                                
                                    
                
                    
                
                    playerClicked = False
        
                    shiporigin = Point(random.randint(-200, 200), random.randint(-300, 300))
        
                    while playerClicked == False:    
                            for i in playerlistoflists:
                                for j in i:
                                    if j.clicked(shiporigin) == True and j not in enemybuttonList:
                                        thirdSpot = i.index(j)
                                        j.deactivate()
                                        #j.place(win)                                        
                                        enemybuttonList.append(j)
                                        playerClicked = not playerClicked                                                  
                            if playerClicked == False:           
                                failedAttempts = failedAttempts + 1
                                if failedAttempts > 5000:
                                    playerClicked = True
                                #print(failedAttempts)
                                shiporigin = Point(random.randint(-200, 200), random.randint(-300, 300))
                            else:
                                break
        
        #there were two main problems with this, one being the program generating a ship that didn't have enough space
        #for each failed attempt to find a valid spot, the failedAttempts variable increases, if there are no valid spots it will eventually increase
        # to 5000
        #also sometimes the program doesn't place enough ships, I have no idea why
        # so when either of those things happens the function restarts, and the program's list of ships is clear
        
        shipsPlaced = len(enemybuttonList)
        
        if (failedAttempts < 5000) and (shipsPlaced > 8):
            finished = True
        else:
            finished = False
            print ("program has inputted invalid ships and is now trying again")
            enemybuttonList.clear()

def programGuess (): # this function will make guesses as to where the player's ships are
    
    #the guesses are just random, I wanted to make them based on previous hits, which I'm confident I could do with more time, but I decided to just move on
    
    innerGuess = random.choice(enemylistoflists)
    enemyGuess = random.choice(innerGuess)
    while enemyGuess in previousGuesses:
        innerGuess = random.choice(enemylistoflists)
        enemyGuess = random.choice(innerGuess)
    if enemyGuess in playerbuttonList:
        enemyGuess.hit()
        print("Opponent gets a hit!")
        global enemyHits
        enemyHits = enemyHits + 1
        previousGuesses.append(enemyGuess)
        playerturn = True
        lastGuess = True
    else:
        enemyGuess.miss()
        print("Opponent misses")
        previousGuesses.append(enemyGuess)
        playerturn = True
        
            
        
        
def main ():
    
    playerHits = 0
    

    gameOver = False
    
   
    
    playerClicked = False
    
    #lets player choose ships, generates opponent ships
    initialize()
    print ("opponent is placing ships")
    programInitialize()
    
 
    #activates all buttons for player to press
    for i in playerlistoflists:
        for j in i:
            j.activate()
    
    
    
    # allows player to guess, checks if guess is a hit or miss
    while gameOver == False:
        print("Click on your guess")
        guess = win.getMouse()
        while playerClicked == False:
            for i in playerlistoflists:
                for j in i:
                    if j.clicked(guess) == True:
                        #print ("got it")
                        j.deactivate()
                        playerClicked = True
                        if j in enemybuttonList:
                            j.hit()
                            print("You got a hit!")
                            playerHits = playerHits + 1
                        else:
                            j.miss()
                            print("You missed")
            if playerClicked == False:           
                print ("invalid guess")
                guess = win.getMouse()
            else:
                break
            
        
        #ends game if player finds all ships
       
        if playerHits > 8:
            gameOver = True
        
        # delays for a bit, as suggested, then generates the progam's guess
        playerClicked = False
        time.sleep(1)
        programGuess()
        
        #ends game if opponent finds all ships
        
        if enemyHits > 8:
            gameOver = True
    #determines who won
    
    if playerHits > enemyHits:
        print ("You win!")
    else:
        print ("Opponent wins!")
     
main()



    
