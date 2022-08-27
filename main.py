import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

CHOICES = [rock, paper, scissors]


def main():
    print("Welcome to Rock, Paper, Scissors\n")

    state = True
    while state:
        user_input = input("Select (1) Rock, (2) Paper, (3) Scissors or (Q)uit: ")
        if user_input.lower() == "q":
            state = False
            continue

        try:
            user_choice = int(user_input) - 1
            if user_choice < 0 or user_choice > 2:
                raise Exception("Invalid Selection")
        except:
            print("Huh?")
            continue

        print(f"\nUser's Selection:\n{CHOICES[user_choice]}")

        computer_choice = random.randint(0, 2)
        print(f"\nComputer's Selection:\n{CHOICES[computer_choice]}")

        if user_choice == computer_choice:
            print("It's a draw.\n")

        elif (
            (user_choice == 0 and computer_choice == 2)
            or (user_choice == 1 and computer_choice == 0)
            or (user_choice == 2 and computer_choice == 1)
        ):
            print("YOU WON!\n")
        else:
            print("You lost. Better luck next time!\n")

        play_again = input("Play again? (Y|n): ")
        if play_again.lower() == "n":
            state = False

        print("\n")


if __name__ == "__main__":
    main()
