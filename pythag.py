from banner import banner
from math import sqrt
if __name__ == "__main__":
    banner("Gavin Orcutt", "Pythagorean Calculator")

def main():
    print("\nWe will help you find the missing side of a right triangle. The lengths of the two legs are 'a' and 'b', and the length of the hypotenuse is 'c'.\n")
    yn = "Y"
    while yn.upper() != "N" and yn.upper() != "NO":
        run_loop()
        yn = input("Would you like to calculate another triangle (Y/N)? ")
    print("Thank you for using the Pythagorean Calculator!")


def run_loop():
    pythag()


def pythag():
    print("Please enter the length of each side, or leave it blank if you don't know.")
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    calculate(a, b, c)


def calculate(a, b, c):
    if a == "" and b != "" and c != "":
        if float(b) >= float(c):
            print("A leg can not be longer than the hypotenuse.") #Makes sure c isn't smaller than a or b
            return
        calc_leg(float(b), float(c), "a")
        return
    if a != "" and b == "" and c != "":
        if float(a) >= float(c):
            print("A leg can not be longer than the hypotenuse.") #Makes sure c isn't smaller than a or b
            return
        calc_leg(float(a), float(c), "b")
        return
    if a != "" and b != "" and c == "":
        calc_hypo(float(a), float(b))
        return
    print("Your input was not valid.") #This happens if there are 0, 2, or 3 blank spots.


def calc_leg(leg, hypo, side):
    ans = sqrt(hypo*hypo-leg*leg) #Pythag theorem
    if tripple_test(leg, hypo, ans) == 1:
        print("Congratulations, you have yourself a Pythagorean Tripple!", end=" ")
    print(f"The length of {side} is {ans}.\n")


def calc_hypo(leg1, leg2):
    ans = sqrt(leg1*leg1+leg2*leg2) #Pythag theorem
    if tripple_test(leg1, leg2, ans) == 1:
        print("Congratulations, you have yourself a Pythagorean Tripple!", end=" ")
    print (f"The length of the c is {ans}.\n")


def tripple_test(a, b, c):
    if (a+b+c) % 1 == 0: #If there's no remainder, it's a tripple.
        return 1


main()



















