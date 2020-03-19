"""
Akash Ashok
"""

import random

class Deque:

    # Uses Python List data structure called 'items' to implement the deque
    def __init__(self):
        self.items = []
        
    # add_front method adds a new item to the deque (at list[SIZE-1])
    def add_front(self, item):
        self.items.append(item)
        
    # add_rear method adds a new item to the deque (at list[0])
    def add_rear(self, item):
        self.items.insert(0,item)
        
    # remove_front method removes and returns an item from the deque (at list[SIZE-1])
    def remove_front(self):
        if len(self.items) != 0:
            return self.items.pop()
        
    # remove_rear method removes and returns an item from the deque (at list[0])
    def remove_rear(self):
        if len(self.items) != 0:
            return self.items.pop(0)
        
    # size method returns the size of the deque
    def size(self):
        return len(self.items)
    
    # peek method returns the front item of the deque (at list[SIZE-1])
    def peek(self):
        if len(self.items) != 0:
            return self.items[len(self.items)-1]
    
    # peeklast method returns the rear item of the deque (at list[0])
    def peeklast(self):
        if len(self.items) != 0:
            return self.items[0]

    """
     printall prints out all the items of the deque 
     with the order beginning from the rear item.
     items are separated by ‘ ‘.
     if index is 0, all the items besides the first one
     (the rear item at list[0]) should be hidden by ‘*’.
    """
    def printall(self, index):
        
        for i in range(len(self.items)):
            if index == 0:
                
                if i == index:
                    print(self.items[index], end = ' ')
                else:
                    print("*", end = ' ')
            else:
                print(self.items[i], end = ' ')
        print()



class Solitaire:
    
    def __init__(self, ncards):
        
        self.ncards = ncards
    
        self.shuffleCards()
        
        self.t = []
        self.__CardNo = len(ncards)
        self.__ColNo = (self.__CardNo // 8) + 3
        self.__ChanceNo = self.__CardNo * 2

        
        
        
        for i in range(self.__ColNo):
            self.t.append(Deque())
        for i in range(self.__CardNo):
            self.t[0].add_front(ncards[i])

            
    """
    display method displays the game layout
    game should have a number (self.__ColNo) of card piles.
    Each card pile is stored as a deque.
    the first row will display the first item only,
    the others are hidden by '*'
    """
    def display(self):
        
        
        for i in range(self.__ColNo):
            print(str(i) + ': ',end= '')
            self.t[i].printall(i)

            
    """
    move method moves the card from a pile to another pile. 
    There are three types of moves.
    
    Condition 1 (c1 = c2 = 0):
    
    move a card from the top of the first pile (rear of the list)
    to the bottom of the first pile (front of the list). This move is always valid.

    Condition 2 (c1 = 0, c2 > 0):

    move a card from the top of the first pile (rear of the list)
    to the bottom of any other pile c2 (front of the list).
    This move is valid only when the number of moving card (N1)
    is less than the number of the card (N2)
    at the bottom of the destination pile by one (i.e., N2 = N1 + 1).

    Condition 3 (c1 > 0, c2 > 0):
    
    move the whole pile of cards from
    c1 to the bottom of any other pile c2 (front of the list).
    This move is valid only when the number of card (N1)
    on the top of the moving pile is less than the number of the card (N2)
    at the bottom of the destination pile by one (i.e., N2 = N1 + 1).
    
    """    
    def move(self, c1, c2):
        
        if c1 == 0 and c2 == 0:
            if self.t[c1].size() > 0:
                rear_value = self.t[0].remove_rear()
                self.t[0].add_front(rear_value)
        
        elif c1 == 0 and  c2 > 0:
            if self.t[c1].size() > 0:
                rear_value = self.t[0].peeklast()
                if self.t[c2].size() > 0:
                    if rear_value + 1 == self.t[c2].peek():
                        self.t[c2].add_front(self.t[0].remove_rear())
                else:
                    self.t[c2].add_front(self.t[0].remove_rear())
                
        elif c1 > 0 and  c2 > 0:
            if self.t[c1].size() > 0:
                rear_value = self.t[c1].peeklast()
                if self.t[c2].size() > 0:
                    if rear_value + 1 == self.t[c2].peek():
                        for i in range(self.t[c1].size()):
                            self.t[c2].add_front(self.t[c1].remove_rear())
                else:
                    for i in range(self.t[c1].size()):
                        self.t[c2].add_front(self.t[c1].remove_rear())


                        
    """
    IsComplete method checks whether the player can win the game.
    The player can win the game if all of below are satisfied:

    1) No card on the first pile
    2) All the cards are on the one of other piles
    3) All the cards are in decreasing order (it should be always true if there is no illegal move)

    This function returns True if the player win the game and False otherwise.
    """
    def IsComplete(self):
        
        game_check1 = False
        if self.t[0].size() == 0:
            game_check1 = True
        
        game_check2 = False    
        for i in range(self.__ColNo):
            if self.t[i].size() == self.__CardNo:
                game_check2 = True
                winning_col = i
        
        if game_check2 == True:
            game_check3 = True
            
        else:
            game_check3 = False
            
        if  game_check1 == True and game_check2 == True and game_check3 == True:
            return True
        else:
            return False
                
    """
    Shuffle function which return shuffled deck of cards.
    """
    def shuffleCards(self):
        return random.shuffle(self.ncards)

    """
    Replay function which allows users to go back 1 move if they have made a error while typing their column number
    """
    def replay_turn(self, col1, col2, count):
        self.t[col1].add_rear(self.t[col2].remove_front())
        count +=1
        return count
    """
    AI Function that plays the game with an alogorithm
    """
    def ai_computer_player(self):
        
        count  = 0
        lst0 = self.ncards
        
        lst1 = []
        lst2 = []
        lst3 = []

        for i in range(len(lst0)):
            
            if len(lst0) == len(lst1) or len(lst0) == len(lst2) or len(lst0) == len(lst3):
                return count
            else:
                if i < 3:
                    if len(lst1) == 0:
                        lst1.append(lst0[i])
                        count +=1
                    
                    elif len(lst2) == 0:
                        lst2.append(lst0[i])
                        count +=1
                    
                    elif len(lst3) == 0:
                        lst3.append(lst0[i])
                        count +=1

                elif ((len(lst1) > 0 and len(lst2) > 0) and (lst1[0] == lst2[-1] + 1)) or  ((len(lst1) > 0 and len(lst3) > 0) and (lst1[0] == lst3[-1] + 1)):       
                    
                        if lst1[0] == lst2[-1] + 1:
                            lst2 = lst2 + lst1
                            lst1 = []
                            count +=1
                        else:
                            lst3 = lst3 + lst1
                            lst1 = []
                            count +=1
                            
                elif ((len(lst1) > 0 and len(lst2) > 0) and (lst2[0] == lst1[-1] + 1)) or ((len(lst2) > 0 and len(lst3) > 0) and (lst2[0] == lst3[-1] + 1)):        

                        if lst2[0] == lst1[-1] + 1:
                            lst1 = lst1 + lst2
                            lst2 = []
                            count +=1
                        else:
                            lst3 = lst3 + lst2
                            lst2 = []
                            count +=1

                            
                elif ((len(lst1) > 0 and len(lst2) > 0) and (lst3[0] == lst2[-1] + 1)) or ((len(lst1) > 0 and len(lst3) > 0) and (lst3[0] == lst1[-1] + 1)):    

                        if lst3[0] == lst2[-1] + 1:
                            lst2 = lst2 + lst3
                            lst3 = []
                            count +=1
                        else:
                            lst1 = lst1 + lst3
                            lst3 = []
                            count +=1        
                else:                    
                    if lst1[-1] + 1 == lst0[i]:
                        lst1.append(lst0[i])
                        count +=1
                    
                    elif lst2[-1] + 1 == lst0[i]:
                        lst2.append(lst0[i])
                        count +=1

                    elif lst3[-1] + 1 == lst0[i]:
                        lst3.append(lst0[i])
                        count +=1
                    
                    else:
                        
                        lst0.append(lst0.pop(i))
                        count +=1
                        
                        
        return count
                
                    
  

                    
        
        
        
        
        
    def play(self):

        print("*****************************************NEW GAME***************************************")
        

        """
        x = self.ai_computer_player()
        """
        
        """
        print()
        play_against_comp = input("Would you like to play against a computer Y or N: ")
        print()
        """
            
        count = 0
        for game_iter in range(self.__ChanceNo):

            self.display()

            print("Round", game_iter+1, "out of", self.__ChanceNo, end = ": ")

            col1 = int(input("Move from row no.:"),10)

            print("Round", game_iter+1, "out of", self.__ChanceNo, end = ": ")

            col2 = int(input("Move to row no.:"),10)

            if col1 >= 0 and col2 >= 0 and col1 < self.__ColNo and col2 < self.__ColNo:

                self.move(col1, col2)
                
            if count < 3:    
                replay = input("Do you wish to replay that move? Y or N ? ")
                print()
                if replay == "Y" or replay == 'y':
                    print("Current Play")
                    print()
                    self.display()
                    
                    count = self.replay_turn(col1, col2, count)
                    
                    print("This is your", count+1, "of 3",  "attempts to replay your move")
                    print()      
                    print("Round", game_iter+1, "out of", self.__ChanceNo, end = ": ")

                    col1 = int(input("Move from row no.:"),10)

                    print("Round", game_iter+1, "out of", self.__ChanceNo, end = ": ")

                    col2 = int(input("Move to row no.:"),10)

                    

                    if col1 >= 0 and col2 >= 0 and col1 < self.__ColNo and col2 < self.__ColNo:

                        self.move(col1, col2)
                
                

            if (self.IsComplete() == True):

                print("You Win in", game_iter+1, "steps!")

                break;

            else:

                if game_iter+1 == self.__ChanceNo:

                   print("You Lose!")



        """
        if play_against_comp == 'Y':
            comp_moves = self.ai_computer_player()
            print("Computer finished this game in",comp_moves)
        print()
        """

cards = [5, 13, 9, 6, 12, 8, 11, 14, 10, 7, 1, 2, 0, 3, 4]
game = Solitaire(cards)
game.play()
