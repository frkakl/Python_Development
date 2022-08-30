import random 

i = random.randrange(0,10)
guess = int(input("Enter Number Between 0-10 = "))
while i != guess:
    if guess < i:
        print("This is too Low")
        guess = int(input("Enter Number Between 0-10 = "))
    elif guess > i:
        print("This is too High")
        guess = int(input("Enter Number Between 0-10 = "))
    else:
        break
print("That's True")
