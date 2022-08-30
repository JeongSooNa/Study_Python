# up & down game

import random

# random number between 0 to 100
result = random.randint(0,100)

# count : count to try
count = 0

# while logic
while True : 
    count +=1
    print("***")
    print("[challenge no",count,"]")
    
    answer = int(input("Please choose number between 0 to 100\nanswer : "))

    if answer == result :
        print("Collect!")
        break
    elif answer > result :
        print("The result is smaller than answer. DOWN! ")
        continue
    else :
        print("The result is bigger than answer. UP! ")
        continue

# Count how long to collect number
print("You got the correct answer in",count,"times.")
