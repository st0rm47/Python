import random

def get_computers_choice():
    random_number = random.randint(1, 3)
    options = {1: "rock", 2: "paper", 3: "scissors"}
    return options[random_number]

def get_user_input():
    while True:
        user_input = input("Enter rock/paper/scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input

def get_result(user_pick, computer_pick):
    if computer_pick == user_pick:
        return "draw"
    elif user_pick == "paper" and computer_pick == "rock":
        return "win"
    elif user_pick == "rock" and computer_pick == "scissors":
        return "win"
    elif user_pick == "scissors" and computer_pick == "paper":
        return "win"
    else:
        return "lose"

def main():
    computer_pick = get_computers_choice()
    user_pick = get_user_input()
    result = get_result(user_pick, computer_pick)
    print(f"Computer's pick: {computer_pick}")
    print(f"Your pick: {user_pick}")
    print(f"You {result}")

if __name__ == "__main__":
    main()

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



                    if self.board.is_winner(self.player.type):
                        print(f"{self.player.name} wins!")
                        break
                    elif self.board.check_draw():
                        print("It's a draw!")
                        break
                    else: