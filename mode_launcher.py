import sys
from new_game import NewGame
from continue_game import ContinueGame
from game_statistics import GameStatistics
from game_rules import GameRules

class ModeLauncher:
    def __init__(self):
        self.modes = {    
                1: NewGame,
                2: ContinueGame,
                3: GameStatistics,
                4: GameRules,
            }

    def display_modes_list(self):
        print()
        print("Screen, not a board, game")
        print()
        print("Available modes:")
        print("1 New Game")
        print("2 Continue Game")
        print("3 Statistics")
        print("4 Game Rules")
        print("5 Exit")
    
    def mode_execution(self, mode_type):
        if mode_type == "5":
            sys.exit("Bye and till the next time")
        try:
            mode_type = int(mode_type)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        mode_class = self.modes.get(mode_type)
        if not mode_class:
            print("Invalid mode selected. Choose again.")
            return
        mode_instance = mode_class()
        if hasattr(mode_instance, "execute"):
            mode_instance.execute()
        else:
            print(f"The selected mode '{mode_type}' does not have an 'execute' method.")