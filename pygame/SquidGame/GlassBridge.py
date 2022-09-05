# Glass Bridge

import random


life = int(input("Survived Number : "))
stageNum = 5

for i in range(stageNum) :

    ran_num = random.uniform(0,1)

    answer = ""
    if ran_num > 0.5 :
        answer = "R"
    else :
        answer = "L"

    choice = input("your choice (R/L) : ")
    if choice == answer :
        life = life
    else :
        life -= 1

    # end game
    if life == 0 :
        print("Game Over..")
        break
    if i == (stageNum-1) :
        print("Game Success!!")
        break

# This logic needs detailed setting
# ex) member's number / unexpected fighting / other situation