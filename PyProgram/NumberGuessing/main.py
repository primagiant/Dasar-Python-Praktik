# Number Guessing
import random

print("==================================")
print("Welcome to Number Guessing Game !!")
print("==================================")

num = random.randint(0, 100)
guess = 0
print(num)

for i in range(5, 0, -1):
    guess = int(input("Please Insert Number in range 1-100 : "))
    if num > guess:
        print("Greater")
    elif num < guess:
        print("Lower")
    else:
        break
    print(f"You have {i-1} change aggain")


if(num == guess):
    print(f"You're right the num is {num}")
else:
    print(f"Try Again Later,the num is {num}")
print(f"Your guess is {guess}")
