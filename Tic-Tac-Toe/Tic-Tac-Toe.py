'''
Created on Aug 29, 2015

@author: namrata jagasia
email: njagasia@indiana.edu
'''

mapp =[[" "," "," "],[" "," "," "],[" "," "," "]];
player_map =[[" "," "," "],[" "," "," "],[" "," "," "]];
turn ="X"
done = False
position = 0

#to print a board having the X player and Y player moves
def print_Board():
    for i in range(0,3):
        for j in range(0,3):
            print mapp[i][j],
            if(j!=2):
                print "|",
        print ""  
        
#to print a board having the human and computer moves         
def print_PlayerBoard():
    for i in range(0,3):
        for j in range(0,3):
            print player_map[i][j],
            if(j!=2):
                print "|",
        print ""           
        
#check if any player wins
def check():
    for i in range(0,3):
        if mapp[0][i] == mapp[1][i] == mapp[2][i] !=" "\
        or mapp[i][0] == mapp[i][1] == mapp[i][2] != " ":
            print turn,"Won!!!"
            return True
        
    if mapp[0][0] == mapp[1][1] == mapp[2][2]!=" " \
    or mapp[2][0] == mapp[1][1] == mapp[0][2]!=" ":
        print turn,"Won!!!"
        return True
            
    if " " not in mapp[0] and " " not in mapp[1] and " " not in mapp[2]:
        print "Draw"
        return True
        
    return False  

# #checks for state of human and computer moves  and provides a position for the best move.
# it checks the state and also checks if the position it is providing is empty or not if not looks for another better move
# If there is just one human move places a move in the center or corners
# Then it checks If there is a possibility to make a winning move it provides that position
# Then it checks if there is a possibility to block the winning move of human it provides that position.
# then as per the human and computer position it will provide a best position.
#lastly it gives a location available when the game is almost complete
def make_Move():
    #print player_map
    
    countH = sum(x.count('h') for x in player_map)
    if countH == 1 and player_map[1][1]==" ":
        return 5
    if countH == 1 and player_map[0][0]==" ":
        return 1
    elif countH ==1 and player_map[0][2]==" ":
        return 3
    elif countH == 1 and player_map[2][0]==" ":
        return 7
    elif countH == 1 and player_map[2][2]==" ":
        return 9
    #Moves to make a winning move eg computer is 1,3 then 2
    # 1,4 or 3,5 or 8,9 then pos 7
    elif (player_map[0][0]==player_map[1][0]=='c' or player_map[0][2]==player_map[1][2]=="c" or player_map[2][1]==player_map[2][2]=="c") and player_map[2][0]==" ":
        return 7
    #  2,5 or 7,9 then pos 8
    elif (player_map[0][1]==player_map[1][1]=='c' or player_map[2][2]==player_map[2][0]=="c") and player_map[2][1]==" ":
        return 8
    # 1,5 or 3,6 or 7,8 then pos 9
    elif (player_map[0][2]==player_map[1][2]=='c' or player_map[0][0]==player_map[1][1]=="c" or player_map[2][0]==player_map[2][1]=="c") and player_map[2][2]==" ":
        return 9
    # 7,4 or 9,5 or 2,3 then pos 1
    elif (player_map[2][0]==player_map[1][0]=='c' or player_map[2][2]==player_map[1][1]=="c" or player_map[0][1]==player_map[0][2]=="c") and player_map[0][0]==" ":
        return 1
    #  8,5 or 1,3 then pos 2
    elif (player_map[1][1]==player_map[2][1]=='c' or player_map[0][0]==player_map[0][2]=="c") and player_map[0][1]==" ":
        return 2
    # 6,9 or 7,5 or 1,2 then pos 3
    elif (player_map[2][2]==player_map[1][2]=='c' or player_map[2][0]==player_map[1][1]=="c" or player_map[0][0]==player_map[0][1]=="c") and player_map[0][2]==" ":
        return 3
    # 7,1 or 6,5 then pos 4
    elif (player_map[2][0]==player_map[0][0]=='c' or player_map[1][2]==player_map[1][1]=="c") and player_map[1][0]==" ":
        return 4
    # 2,8 or 4,6 or 1,9 or 3,7 then pos 5
    elif (player_map[0][1]==player_map[2][1]=='c' or player_map[1][0]==player_map[1][2]=="c" or player_map[0][0]==player_map[2][2]=="c" or player_map[0][2]==player_map[2][0]=="c") and player_map[1][1]==" ":
        return 5
    # 5,4 or 9,3 then pos 6
    elif (player_map[1][1]==player_map[1][0]=='c' or player_map[2][2]==player_map[0][2]=="c") and player_map[1][2]==" ":
        return 6
      
    #Moves to block human move
    # 1,4 or 3,5 or 8,9 then pos 7
    elif (player_map[0][0]==player_map[1][0]=='h' or player_map[0][2]==player_map[1][2]=="h" or player_map[2][1]==player_map[2][2]=="h") and player_map[2][0]==" ":
        return 7
    #  2,5 or 7,9 then pos 8
    elif (player_map[0][1]==player_map[1][1]=='h' or player_map[2][2]==player_map[2][0]=="h") and player_map[2][1]==" ":
        return 8
    # 1,5 or 3,6 or 7,8 then pos 9
    elif (player_map[0][2]==player_map[1][2]=='h' or player_map[0][0]==player_map[1][1]=="h" or player_map[2][0]==player_map[2][1]=="h") and player_map[2][2]==" ":
        return 9
    # 7,4 or 9,5 or 2,3 then pos 1
    elif (player_map[2][0]==player_map[1][0]=='h' or player_map[2][2]==player_map[1][1]=="h" or player_map[0][1]==player_map[0][2]=="h") and player_map[0][0]==" ":
        return 1
    #  8,5 or 1,3 then pos 2
    elif (player_map[1][1]==player_map[2][1]=='h' or player_map[0][0]==player_map[0][2]=="h") and player_map[0][1]==" ":
        return 2
    # 6,9 or 7,5 or 1,2 then pos 3
    elif (player_map[2][2]==player_map[1][2]=='h' or player_map[2][0]==player_map[1][1]=="h" or player_map[0][0]==player_map[0][1]=="h") and player_map[0][2]==" ":
        return 3
    # 7,1 or 6,5 then pos 4
    elif (player_map[2][0]==player_map[0][0]=='h' or player_map[1][2]==player_map[1][1]=="h") and player_map[1][0]==" ":
        return 4
    # 2,8 or 4,6 or 1,9 or 3,7 then pos 5
    elif (player_map[0][1]==player_map[2][1]=='h' or player_map[1][0]==player_map[1][2]=="h" or player_map[0][0]==player_map[2][2]=="h" or player_map[0][2]==player_map[2][0]=="h") and player_map[1][1]==" ":
        return 5
    # 5,4 or 9,3 then pos 6
    elif (player_map[1][1]==player_map[1][0]=='h' or player_map[2][2]==player_map[0][2]=="h") and player_map[1][2]==" ":
        return 6
    
    
    # if any of the two corners has h then put c in 2,4,6,8
    #ie 1,9 or 3,7
    elif (player_map[0][0]==player_map[2][2]=='h' or player_map[0][2]==player_map[2][0]=="h"):
        if player_map[0][1]==" ":
            return 2
        elif player_map[1][0]==" ":
            return 4
        elif player_map[1][2]==" ":
            return 6
        elif player_map[2][1]==" ":
            return 8        
    elif mapp[0][0]==" ":
        return 1
    elif mapp[0][2]==" ":
        return 3
    elif mapp[2][0]==" ":
        return 7
    elif mapp[2][2]==" ":
        return 9
    elif player_map[0][1]==" ":
            return 2
    elif player_map[1][0]==" ":
            return 4
    elif player_map[1][2]==" ":
            return 6
    elif player_map[2][1]==" ":
            return 8   
    else:
        return 5

                
#ask for position, check if its done if not get a position from human or from computer and mark the position.
decideVariable = input("To be the first Player X Enter 1 \n To be the second Player 0 Enter 0 ")
first_move = False
computer_move = False
while done!=True:
    print " Turn of "+turn+" \n 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9 "
    print ""
    moved = False
    
    while moved!=True:
        try:            
            if decideVariable == 0 and first_move!=True:
                pos = 1
                first_move= True
                
            elif computer_move==True:
#               call a  function that sees the state of the board and provides a position
                computer_move = not computer_move    
                pos= make_Move()                      
                            
            else : 
                computer_move = not computer_move             
                pos = input("Select the position for your move")
                
            if pos>=1 and pos<=9:
                Y = pos/3
                X = pos%3
                if X!=0:
                    X -=1
                else:
                    X= 2
                    Y = Y - 1
                        
                if mapp[Y][X]==" ":
                    #print Y
                    #print X
                    
                    mapp[Y][X] = turn
                    moved=True
                    done = check()
                    if turn == "X":
                        if decideVariable == 1:
                            player_map[Y][X]="h"
                        else:
                            player_map[Y][X]="c"
                             
                        turn ="0"
                    else: 
                        if decideVariable == 1:
                            player_map[Y][X]="c"
                        else:
                            player_map[Y][X]="h"                        
                        turn = "X"    
                    print_Board()
                    print " "
               #    print_PlayerBoard()
                    print " "
        except:
                print "You need to add a numeric value"      
                print " "          
                
                               # @IndentOk