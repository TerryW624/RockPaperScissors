

class Gesture:
    def __init__(self, name):
        self.name = name

        # if gestures.index(gesture1) - gestures.index(gesture2) == 2 or gestures.index(gesture1) - gestures.index(gesture2) == 4:
        #     print(f"{player_1.name} wins")
        
        # elif gestures.index(gesture1) - gestures.index(gesture2) == -1 or gestures.index(gesture1) - gestures.index(gesture2) == -3:
        #     print(f"{player_1.name} wins")

        # elif gestures.index(gesture1) == gestures.index(gesture2):
        #     print("Tied")

        # else:
        #     print(f"{player_2.name} wins")
         


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

