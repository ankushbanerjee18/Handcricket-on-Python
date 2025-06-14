import random

def hc():
    a = random.randint(1,6)
    score = 0 
    runs = int(input("Enter a number from 0-6: "))
    while runs != a:
        score = score + runs
        print(f"Your score is {score}")
        print(f"You played {runs}, computer played {a}")
        runs = int(input("Enter a number from 0-6: "))
        a = random.randint(1,6)
        if runs == a:
            print(f"You are out, your total score is {score}")