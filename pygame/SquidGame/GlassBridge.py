# Glass Bridge

import random


life = int(input("Survived Number : "))
stageNum = 5

for i in range(stageNum) :
    # end game
    if life == 0 :
        print("Game Over..")
    if i == (stageNum-1) :
        print("Game Success!!")

    ran_num = random.uniform(0,1)

    answer = ""
    if ran_num > 0.5 :
        answer = "R"
    else :
        answer = "L"

    choice = input("your choice (R/L) : ")
    if choice == answer :
        continue
    else :
        life -= 1
        continue