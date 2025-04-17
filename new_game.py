class NewGame:
    def execute(self):
        while True:
            print("this is new game mode")
            choice = input("Type 'back' to return to the main menu: ")
            if choice.lower() == "back":
                break