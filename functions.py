def binary_answer(user_input, yes, no):
    global yes_or_no
    running = True
    while running:
        if user_input == "yes" or "y" or "ye":
            yes_or_no = 1
            print(yes)
            running = False
        elif user_input == "no" "n":
            yes_or_no = 0
            print(no)
            running = False
        else:
            print("Please answer yes or no.")
            user_input = input()
print("Are you sure you want to do this?")
binary_answer(input(), "All right, let us begin", "So that is how it is.")