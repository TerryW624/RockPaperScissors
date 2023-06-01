from random import choice

gestures = ["rock", "paper", "scissors", "lizard", "spock"]

class Player:
    def __init__(self):
        self.name = ''
        self.score = 0

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        while True:
            choice = input(f"{self.name} what gesture do you would you like?\n {gestures} > ")
            if choice.lower() in gestures:
                return choice.lower()
            else:
                print("Invalid choice, please try again.")


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        choice(gestures)