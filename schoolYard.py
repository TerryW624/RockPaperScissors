from player import *
from sandbox import *
import time




class Rpsls:
    def __init__(self):
        self.gestures = []
        self.player_1 = None
        self.player_2 = None
    
    def two_out_three(self):
        player_2_score = self.player_2.score
        player_1_score = self.player_1.score
        while True:
            gesture_1 = self.player_1.choose_gesture()
            gesture_2 = self.player_2.choose_gesture()

            if self.player_2.name == "AI bot":
                print(f"{self.player_2.name} chose {gesture_2}") 
                timer(.5)
            round_win = Gesture.decide_win_or_lose(self, gestures, gesture_1, gesture_2, self.player_1, self.player_2)
            # if (gesture1 == "rock" and (gesture2 == "scissors" or gesture2 == "lizard")) or (gesture1 == "scissors" and (gesture2 == "paper" or gesture2 == "lizard")) or (gesture1 == "paper" and (gesture2 == "rock" or gesture2 == "spock")) or (gesture1 == "spock" and (gesture2 == "rock" or gesture2 == "scissors")) or (gesture1 == "lizard" and (gesture2 == "spock" or gesture2 == "paper")):
            if round_win == self.player_1.name:
                player_1_score += 1
            elif round_win == self.player_2.name:
                player_2_score += 1
            else:
                print("Tied")
            timer(.5)
            # elif gesture1 == gesture2:
            #     print("Tie")
            #     continue
            # else:
            print(f"{self.player_1.name} {player_1_score} {self.player_2.name} {player_2_score}")
            timer(.5)
            if player_1_score >= 2 or player_2_score >= 2:
                timer(.5)
                break
        if player_1_score > player_2_score:
            timer(.5)
            print(f"{self.player_1.name} wins\nWoohoo")
        else:
            timer(.5)
            print(f"{self.player_2.name} wins\nWoohoo")

    def welcome(self):
        self.player_1 = HumanPlayer()
        self.player_1.name = input("What is your name? > ")
        timer(.5)
        print('-+-+-Welcome to Rock Paper Scissors Lizard Spock-+-+-')
        timer(.5)
        print('        Rules:')
        timer(.5)
        print('Rock crushes Scissors')
        timer(.2)
        print('Scissors cuts Paper ')
        timer(.2)
        print('Paper covers Rock')
        timer(.2)
        print('Rock crushes Lizard')
        timer(.2)
        print('Lizard poisons Spock')
        timer(.2)
        print('Spock smashes Scissors')
        timer(.2)
        print('Scissors decapitates Lizard')
        timer(.2)
        print('Lizard eats Paper')
        timer(.2)
        print('Paper disproves Spock')
        timer(.2)
        print('Spock vaporizes Rock')
    
    def choose_players(self):
        while True:
            player_2_choice = input(f'\nDo you want to play 1 player mode or 2 player mode? > ') 
            timer(.5)
            if player_2_choice == '1':
                timer(.5)
                self.player_2 = ComputerPlayer("AI bot")
            elif player_2_choice == '2':
                timer(.5)
                self.player_2 = HumanPlayer()
                self.player_2.name = input("What is the second player's name? > ")
                timer(.5)
            else:
                timer(.5)
                print('Invalid. Try again...')
                continue
            break

    def run_game(self):
        self.welcome()
        timer(.5)
        self.choose_players()
        timer(.5)
        self.two_out_three()
