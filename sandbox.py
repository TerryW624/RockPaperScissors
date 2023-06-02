

class Gesture:
    def __init__(self, name):
        self.name = name

    def decide_win_or_lose(self, gestures, gesture1, gesture2, player_1, player_2):
        if gestures.index(gesture1) - gestures.index(gesture2) == 2 or gestures.index(gesture1) - gestures.index(gesture2) == 4:
            return player_1.name  
        elif gestures.index(gesture1) - gestures.index(gesture2) == -1 or gestures.index(gesture1) - gestures.index(gesture2) == -3:
            return player_1.name
        elif gestures.index(gesture1) == gestures.index(gesture2):
            return "tied"
        else:
            return player_2.name

class Rock(Gesture):
    def __init__(self, name):
        super().__init__(name)

class Paper(Gesture):
    def __init__(self, name):
        super().__init__(name)

class Scissors(Gesture):
    def __init__(self, name):
        super().__init__(name)

class Lizard(Gesture):
    def __init__(self, name):
        super().__init__(name)

class Spock(Gesture):
    def __init__(self, name):
        super().__init__(name)

