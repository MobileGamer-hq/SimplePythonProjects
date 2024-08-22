import random



possible_pos = [1,2,3,4,5,6,7,8,9]
winning_pos = [[1,2,3], [4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
player_used_pos = []
computer_used_pos = []

computer = "computer"
player = "player"

def checkPos(pos = []):
    for i in winning_pos: 
            check = 0 
                  
            for j in i:
                    for k in pos:
                        if k == j:
                            check += 1

                            if check == 3: return True
                            break

    return False

def displayBoard():
    board = {"1": " ", "2": " ","3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
    for i in player_used_pos:
         board[str(i)] = "o"
    for i in computer_used_pos:
         board[str(i)] = "x"    
    return f'''
     {board[str(1)]}|{board[str(2)]}|{board[str(3)]}
     - - -
     {board[str(4)]}|{board[str(5)]}|{board[str(6)]}
     - - -
     3{board[str(7)]}|{board[str(8)]}|{board[str(9)]}
    '''

def playMove(player, move):
    for i in possible_pos:
        if move == i:
            if player == computer:
                computer_used_pos.append(move)
            else:
                player_used_pos.append(move)
                

            possible_pos.remove(move)
            print(displayBoard())
            return True
    return False
    
        
    



def start():
    while(True):
        computer_play = random.choice(possible_pos)
        
        playMove(computer, computer_play)
        print(f"Computer Played {computer_play}, {computer_used_pos}, {possible_pos}")

        if checkPos(computer_used_pos): 
            print("Computer Won!!!")
            break
        
        print(f"Possible moves now: {possible_pos}")
        player_play = int(input("play your next position: "))
        playMove(player, player_play)

        


        if checkPos(player_used_pos): 
            print("You Won!!!")
            break

        if len(possible_pos) <= 0: 
            print("Draw!!!")
            break
   

start()
