from player import *




class Rpsls:
    def __init__(self):
        self.gestures = gestures
        self.humanPlayer = HumanPlayer()
    
    def two_out_three(self):
        while True:
            pass
        
    def welcome(self):
        player_2 = Player()
        player_1 = HumanPlayer()
        player_1.name = input('What is your name? > ')
        player_2_choice = input(f'-+-+-Welcome to Rock Paper Scissors Lizard Spock-+-+- \nDo you want to play one player mode or two player mode? > ')
        if player_2_choice == '1':
            player_2 = ComputerPlayer(player_2.name)
        else:
            player_2 = HumanPlayer(player_2.name)

        player_1 = HumanPlayer(player_1.name)
        player_2 = HumanPlayer(player_2.name)

    def run_game(self):
        self.two_out_three()
        self.welcome()