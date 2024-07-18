import random

def play_round(user_choice):
  """Plays a single round of rock-paper-scissors.

  Args:
      user_choice (str): User's choice (rock, paper, or scissors).

  Returns:
      tuple: A tuple containing the result ("Win", "Lose", or "Tie") and the computer's choice.
  """
  # Define valid choices
  choices = ["rock", "paper", "scissors"]

  # Validate user input
  if user_choice.lower() not in choices:
    return "Invalid choice. Please choose rock, paper, or scissors.", None

  # Generate computer's choice
  computer_choice = random.choice(choices)

  # Determine winner
  if user_choice.lower() == computer_choice:
    return "Tie", computer_choice
  elif (user_choice.lower() == "rock" and computer_choice == "scissors") or \
       (user_choice.lower() == "paper" and computer_choice == "rock") or \
       (user_choice.lower() == "scissors" and computer_choice == "paper"):
    return "Win", computer_choice
  else:
    return "Lose", computer_choice

def main():
  """Runs the rock-paper-scissors game loop with optional score tracking."""
  # Initialize scores (optional)
  user_score = 0
  computer_score = 0

  # Game loop
  while True:
    print("\n** Rock, Paper, Scissors! **")
    print("  (Enter 'q' to quit)")

    # Get user choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Handle quit option
    if user_choice == 'q':
      break

    # Play a round and get results
    result, computer_choice = play_round(user_choice)

    # Update scores (optional)
    if result == "Win":
      user_score += 1
    elif result == "Lose":
      computer_score += 1

    # Display results
    print(f"\nYou chose {user_choice.capitalize()}. Computer chose {computer_choice.capitalize()}. {result}")

    # Show scores (optional)
    if user_score > 0 or computer_score > 0:
      print(f"Current score: You - {user_score}, Computer - {computer_score}")

    # Ask to play again
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
      break

  # Display final message
  print("\nThanks for playing!")

if __name__ == "__main__":
  main()