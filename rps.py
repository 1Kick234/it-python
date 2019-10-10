import banner
import random

banner.banner("Rock Paper Scissors", "Gavin Orcutt")
print("Rock > Scissors > Paper > Rock. Best 2 out of 3.")
c_score = 0
p_score = 0

def main():
    while c_score < 2 and p_score < 2:
        player_choice = get_player_input()
        computer_pick = get_computer_pick()
        determine_outcome(player_choice, computer_pick)
        print(f"Computer score is {c_score}. Player score is {p_score}.")
    if c_score == 2:
        print(f"You lose the match {p_score} to {c_score}.")
    else:
        print(f"You win the match {p_score} to {c_score}.")


def get_player_input():
    return int(input("1. Rock\n2. Paper\n3. Scissors\n> "))

def get_computer_pick():
    return random.randint(1,3)

def determine_outcome(player_choice, computer_choice):
    global p_score
    global c_score

    if player_choice == 1:
        if computer_choice == 1:
            print("Rock vs. Rock. Tie.")
        elif computer_choice==2:
            print("Rock vs. Paper. Loss")
            c_score += 1
        else:
            print("Rock vs. Scissors. Win.")
            p_score += 1

    if player_choice == 2:
        if computer_choice == 1:
            print("Paper vs. Rock. Win.")
            p_score += 1
        elif computer_choice==2:
            print("Paper vs. Paper. Tie.")
        else:
            print("Paper vs. Scissors. Loss.")
            c_score += 1

    if player_choice == 3:
        if computer_choice == 1:
            print("Scissors vs. Rock. Loss.")
            c_score += 1
        elif computer_choice==2:
            print("Scissors vs. Paper. Win")
            p_score += 1
        else:
            print("Scissors vs. Scissors. Tie.")

main()