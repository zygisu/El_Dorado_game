#########BLACK ALL FILES AFTER implementing everything

import time
import os
import pyfiglet
from mode_launcher import ModeLauncher

class Main:
    def __init__(self):
        self.mode_launcher = ModeLauncher()

    def welcome_message(self):
        
        text = "El Dorado " 
        title = pyfiglet.figlet_format(text)
        
        print(title)  
        time.sleep(4)
        os.system("cls" if os.name == "nt" else "clear")

    def run(self):
        self.welcome_message()
        while True:
            self.mode_launcher.display_modes_list()
            mode_type = input("\nChoose mode and press ENTER (or type 'exit' to quit): ")
            if mode_type.lower() == "exit":
                print("Exiting the game.")
                break
            try:
                self.mode_launcher.execute_mode(mode_type)
            except SystemExit:
                print("Exiting the game.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid mode.")
            except KeyError as e:
                print(f"Mode not found: {e}. Please choose a valid mode.")
            except Exception as e:
                print(f"Unexpected error: {e}. Try again.")



if __name__ == "__main__":
    program = Main()
    program.run()