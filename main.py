class Game:
    def __init__(self):
        self.player = None
        self.current_room = None

    def setup(self):
        # Initialize player and starting room
        self.player = Player("Hero", 100)  # Name and HP
        self.current_room = Room("Starting Room", "You are in a dimly lit room.")

    def game_loop(self):
        self.setup()
        while True:
            print(f"\n{self.current_room.name}")
            print(self.current_room.description)
            command = input("> ").lower().strip()
            if command == "quit":
                break
            self.process_command(command)

    def process_command(self, command):
        if command == "look":
            print(self.current_room.description)
        elif command == "inventory":
            self.player.show_inventory()
        else:
            print("I don't understand that command.")

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.inventory = []

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item}")

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

if __name__ == "__main__":
    game = Game()
    game.game_loop()

