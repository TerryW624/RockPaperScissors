from random import choice
import time

gestures = ["rock", "paper", "scissors", "lizard", "spock"]

class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0

class HumanPlayer(Player):
    def __init__(self):
        super().__init__(__name__)

    def choose_gesture(self):
        while True:
            timer(.5)
            choice = input(f"{self.name} what gesture do you would you like?\n{gestures} > ")
            if choice.lower() in gestures:
                timer(.5)
                return choice.lower()
            else:
                time.sleep(1)
                print("Invalid choice, please try again.")


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        comp_choice = choice(gestures)
        return comp_choice
    
def timer(seconds):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = seconds - elapsed_time
        if remaining_time <= 0:
            break
        time.sleep(seconds)