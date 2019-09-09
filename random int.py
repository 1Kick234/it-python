import random
a = random.randint(1,100)
g = input("Guess the number, 1-100> ")
g = int(g)
pg = g
while g != a:
    if g > 100 or g < 1:
        print("Are you stupid?")
    elif g > a:
        if pg < g and prev == 1:
            print("Are you stupid?")
            prev = 1
        else:
            print("Too high.")
            pg = g
            prev = 1
    else:
        if pg > g and prev == 0:
            print("Are you stupid?")
            prev = 0
        else:
            print("Too low.")
            pg = g
            prev = 0
    g = input("Guess the number, 1-100> ")
    g = int(g)
print("Correct!")