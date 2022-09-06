# Statues

import time
import random
from multiprocessing import Process


# Time Check Logic

t = []
for i in range(10) :
    t.append(random.uniform(0,2))

while True :
    time.sleep(t[0])
    print("무")
    time.sleep(t[1])
    print("궁")
    time.sleep(t[2])
    print("화")
    time.sleep(t[3])
    print("꽃")
    time.sleep(t[4])
    print("이")
    time.sleep(t[5])
    print("피")
    time.sleep(t[6])
    print("었")
    time.sleep(t[7])
    print("습")
    time.sleep(t[8])
    print("니")
    time.sleep(t[9])
    print("다")
    print("!!")
    answer = input("keep going!(y/n) : ")
    if answer == "y" :
        continue
    else :
        break

# Run Logic
distance = 0
footprint = ""

def run() :
    run = input("please typing r&l\nex) rlrlrlrl...\nrun!\n")
    # keepgoing
    # you need time check end logic & continue
    return run
footprint += run()

print(footprint)

# Issue
## Create logic to connect other programs or use reference
## 결승선까지 이동하는 개념의 또 다른 실행이 동시적으로 발생해야한다.
## >> multiprocessing 으로 해결해보자!