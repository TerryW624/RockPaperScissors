from player import *




class Rpsls:
    def __init__(self):
        self.gestures = []
        self.player_1 = None
        self.player_2 = None

    def score_increment(self, player):
        score = player.score
        score += 1
        return score
    
    def two_out_three(self):
        while True:
            gesture1 = self.player_1.choose_gesture()
            gesture2 = self.player_2.choose_gesture()
            if self.player_2.name == "AI bot":
                print(f"{self.player_2.name} chose {gesture2}") 
            if (gesture1 == "rock" and (gesture2 == "scissors" or gesture2 == "lizard")) or (gesture1 == "scissors" and (gesture2 == "paper" or gesture2 == "lizard")) or (gesture1 == "paper" and (gesture2 == "rock" or gesture2 == "spock")) or (gesture1 == "spock" and (gesture2 == "rock" or gesture2 == "scissors")) or (gesture1 == "lizard" and (gesture2 == "spock" or gesture2 == "paper")):
                self.score_increment(self.player_1)
            elif gesture1 == gesture2:
                print("Tie")
                continue
            else:
                self.score_increment(self.player_2)
            print(f"{self.player_1.name} {self.player_1.score} {self.player_2.name} {self.player_2.score}")
            if self.player_1.score >= 2 or self.player_2.score >= 2:
                break
        if self.player_1.score > self.player_2.score:
            print(f"{self.player_1.name} wins")
        else:
            print(f"{self.player_2.name} wins")

    def welcome(self):
        self.player_1 = HumanPlayer()
        self.player_1.name = input("What is your name? > ")
        print("-+-+-Welcome to Rock Paper Scissors Lizard Spock-+-+-")
        
    
    def choose_players(self):
        player_2_choice = input(f'\nDo you want to play one player mode or two player mode? > ') 
        if player_2_choice == '1':
            self.player_2 = ComputerPlayer("AI bot")
        else:
            self.player_2 = HumanPlayer()
            self.player_2.name = input("What is the second player's name?")

    def run_game(self):
        self.welcome()
        self.choose_players()
        self.two_out_three()
       