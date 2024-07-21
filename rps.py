# Import the random module for generating random numbers.
import random

# Define the list of possible moves.
moves = ["rock", "paper", "scissors"]


def get_num_rounds():
    """
    Get the number of rounds for the game.

    Returns:
        int: The number of rounds entered by the user.
    """
    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds > 0:
                return rounds
            print("Please enter a positive number of rounds.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_again():
    """
    Asks the user if they want to play again and returns a boolean.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    return input("Would you like to play again? (yes/no): ").lower() == "yes"


def validate_move(move):
    """Validates the input to ensure it's a valid move."""
    return move in moves


def get_player_move():
    """Prompt the user for their move and validate it."""
    while True:
        move = input("Enter your move (rock, paper, scissors): ").lower()
        if validate_move(move):
            return move
        print("Invalid move. Please try again.")


class Player:
    """A base class for all players in the game."""

    def __init__(self):
        self.score = 0
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)

    def move(self):
        """Return the player's move. Should be overridden by subclasses."""
        return 'rock'

    def learn(self, my_move, their_move):
        """Update the player's knowledge based on the last round."""
        self.their_move = their_move


class HumanPlayer(Player):
    """A human player that inputs moves via the console."""

    def move(self):
        """Prompt the user for a move and return it."""
        return get_player_move()


class RandomPlayer(Player):
    """A player that makes random moves."""

    def move(self):
        """Return a random move."""
        return random.choice(moves)


class ImitatingPlayer(Player):
    """A player that imitates the opponent's last move."""

    def move(self):
        """Return the last move of the opponent or a random move if it's
        the first round."""
        return self.their_move


class CyclingPlayer(Player):
    """A player that cycles through moves in order."""

    def __init__(self):
        super().__init__()
        self.my_move = random.choice(moves)

    def move(self):
        """Return the next move in the cycle."""
        index = (moves.index(self.my_move) + 1) % len(moves)
        self.my_move = moves[index]
        return self.my_move


class RockPlayer(Player):
    """A player that always plays 'rock'."""

    def move(self):
        """Return 'rock' as the move."""
        return "rock"


def beats(one, two):
    """Determine if the first move beats the second move."""
    return two in {
        'rock': ['scissors'],
        'scissors': ['paper'],
        'paper': ['rock']
    }.get(one, [])


class Game:
    """Represents a game of Rock-Paper-Scissors."""

    def __init__(self, p1, p2, p1_name, p2_name):
        self.p1 = p1
        self.p2 = p2
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.game_scores = []

    def play_round(self):
        """Play a single round of the game."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"{self.p1_name}: {move1}  {self.p2_name}: {move2}")

        if move1 == move2:
            print("It's a tie!")
        elif beats(move1, move2):
            print(f"{self.p1_name} wins!")
            self.p1.score += 1
        else:
            print(f"{self.p2_name} wins!")
            self.p2.score += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.game_scores.append((self.p1.score, self.p2.score))

    def play_game(self, num_rounds):
        """Play a full game consisting of multiple rounds."""
        print("Game start!")
        for round_num in range(num_rounds):
            print(f"\nRound {round_num + 1}:")
            self.play_round()
            print(f"Score - {self.p1_name}: {self.p1.score}, {self.p2_name}: "
                  f"{self.p2.score}")
        print("\nGame over!")
        self.announce_winner()

    def announce_winner(self):
        """Announce the winner of the game based on the scores."""
        if self.p1.score > self.p2.score:
            print(f"{self.p1_name} wins the game!")
        elif self.p2.score > self.p1.score:
            print(f"{self.p2_name} wins the game!")
        else:
            print("The game is a tie!")


def main():
    """Main game loop."""
    player_name = input("Enter your name: ")
    overall_scores = {player_name: 0, "Computer": 0}
    games_played = 0

    while True:  # Main game loop
        strategies = {
            1: RockPlayer(),
            2: RandomPlayer(),
            3: ImitatingPlayer(),
            4: CyclingPlayer(),
        }

        print("Choose a level of difficulty:")
        print("1. The Rock")
        print("2. Random")
        print("3. The Imitator")
        print("4. Cycling Anyone")

        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    computer_player = strategies[choice]
                    break
                print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        rounds = get_num_rounds()
        game = Game(HumanPlayer(), computer_player, player_name, "Computer")
        game.play_game(rounds)

        # Update overall scores
        overall_scores[player_name] += game.p1.score
        overall_scores["Computer"] += game.p2.score
        games_played += 1

        # Display overall scores
        print("\nOverall Scores:")
        print(f"{player_name}: {overall_scores[player_name]}")
        print(f"Computer: {overall_scores['Computer']}")
        print(f"Games played: {games_played}")

        print("\nScores for each game:")
        for i, (p1_score, p2_score) in enumerate(game.game_scores, 1):
            print(f"Game {i}: {player_name} - {p1_score}, Computer - "
                  f"{p2_score}")

        if not play_again():
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()

# End-of-file (EOF)
