import banner
import random

banner.banner("Rock Paper Scissors", "Gavin Orcutt")
c_score = 0
p_score = 0
rps = ["Rock", "Paper", "Scissors"]
print(f"{rps[0]} > {rps[1]} > {rps[2]} > {rps[0]}. Best 2 out of 3.")

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
    print("Pick the number of your choice.")
    for num, i in enumerate(rps):
        print(f"{num}. {i}")

    return int(input())

def get_computer_pick():
    return random.randint(0,2)

def determine_outcome(player_choice, computer_choice):
    global p_score
    global c_score

    if player_choice == computer_choice:
        print(f"Draw. You both picked {rps[player_choice]}.")
    elif player_choice == 2:
        if player_choice - (computer_choice+3) == -1:
            print(f"You lose. You picked {rps[player_choice]}, computer picked {rps[computer_choice]}.")
            c_score += 1
        else:
            print(f"You win. You picked {rps[player_choice]}, computer picked {rps[computer_choice]}.")
            p_score += 1
    else:
        if player_choice - computer_choice == -1:
            print(f"You lose. You picked {rps[player_choice]}, computer picked {rps[computer_choice]}.")
            c_score += 1
        else:
            print(f"You win. You picked {rps[player_choice]}, computer picked {rps[computer_choice]}.")
            p_score += 1

main()