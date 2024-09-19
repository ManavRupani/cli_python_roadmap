import random

class Game:
    def __init__(self):
        self.target = 0
        self.max_chances = 0
        self.current_chances = 0
        self.difficulty = ""
        self.difficulties = ["Easy", "Medium", "Hard"]

    def set_difficulty(self, new_difficulty):
        if new_difficulty in ["easy", "Easy"]:
            self.difficulty = self.difficulties[0]
            self.max_chances = 10
        elif new_difficulty in ["medium", "Medium"]:
            self.difficulty = self.difficulties[1]
            self.max_chances = 50
        elif new_difficulty in ["hard", "Hard"]:
            self.difficulty = self.difficulties[2]
            self.max_chances = 3
        else:
            print("Invalid response.")

    def check_guess(self, user_input):
        self.current_chances += 1
        if user_input == self.target:
            return True
        elif user_input < self.target:
            print("Too low!")
        else:
            print("Too high!")
        return False

    def get_max(self):
        return self.max_chances

    def get_current_chances(self):
        return self.current_chances

    def start_game(self):
        self.target = random.randint(0, 100)  # Random target number between 0 and 100
        print(f"Game started with difficulty: {self.difficulty}. You have {self.max_chances} chances to guess.")

        while self.current_chances < self.max_chances:
            try:
                user_input = int(input(f"Try to guess (Chances remaining: {self.max_chances - self.current_chances}): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if self.check_guess(user_input):
                print(f"Congratulations! You've guessed the correct number {self.target}.")
                break
        else:
            print(f"Sorry! You've used all your chances. The correct number was {self.target}.")

if __name__ == "__main__":
    game = Game()

    # Prompt user to select difficulty
    while True:
        difficulty = input("Select difficulty (Easy, Medium, Hard): ").strip()
        if difficulty in ["easy", "Easy", "medium", "Medium", "hard", "Hard"]:
            game.set_difficulty(difficulty)
            break
        else:
            print("Invalid difficulty. Please choose from Easy, Medium, or Hard.")

    game.start_game()
