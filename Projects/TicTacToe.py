###---> Tic-Tac-Toe Game <---###

import random

#Creating a Board
class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        
    def print_board(self):
        print(" "+ self.board[0] +  " | " + self.board[1] +  " | " + self.board[2])
        print("-----------")
        print(" "+ self.board[3] +  " | " + self.board[4] +  " | " + self.board[5])
        print("-----------")
        print(" "+ self.board[6] +  " | " + self.board[7] +  " | " + self.board[8])
        
    def update_board(self, position, type):
        if self.board[position - 1] == " ":
            self.board[position - 1] = type
            return True
        else:
            print("Position already taken!")
            return False
        
    def is_winner(self, type):
        #Checking the rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == type:
                return True
        #Checking the columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == type:
                return True
        #Checking the diagonals
        if self.board[0] == self.board[4] == self.board[8] == type:
            return True
        if self.board[2] == self.board[4] == self.board[6] == type:
            return True
        return False
    
    def check_draw(self):
        return " " not in self.board   

#Creating a Player
class Player:
    def __init__(self,type):
        self.type = type
        self.name = self.get_name()
        
    def get_name(self):
        if self.type == "X":
            return input("Enter your name: ")
        else:
            return "Computer"

#Creating a Game
class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player("X")
        self.computer = Player("O")
        
    def play(self):
        #using infinite loop to run the game
        while True:
            try:
                message = f"{self.player.name},\nEnter the position(1-9): "
                if self.player.type == "X":
                    position = int(input(message))
                
                    if self.board.update_board(position, self.player.type):
                        self.board.print_board()

                        if self.board.is_winner(self.player.type):
                            print(f"{self.player.name} wins!")
                            break
                        elif self.board.check_draw():
                            print("It's a draw!")
                            break
                        else:                   
                            #Changing the player to computer
                            self.player, self.computer = self.computer, self.player
                    

                else:
                    position = random.randint(1, 9)
                    if self.board.update_board(position, self.player.type):
                        print(f"{self.player.name} chose position: {position}")
                        self.board.print_board()
                        
                        if self.board.is_winner(self.player.type):
                            print(f"{self.player.name} wins!")
                            break
                        elif self.board.check_draw():
                            print("It's a draw!")
                            break
                        else:                   
                            #Changing the player to USER
                            self.player, self.computer = self.computer, self.player
            
            except:
                print("Invalid Number! Please enter a number between 1-9")
                pass            

#Running the game    
def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()