# Sugar Candy

import numpy as np

# Choose shape
list = ["●","▲","★","♠"]
print("Please choose number")
print("1.",list[0]," 2.",list[1]," 3.",list[2]," 4.",list[3])
choice = int(input("1/2/3/4 : "))
print("Your Choosed shape is",list[choice-1])

# use numpy package for create share
a = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    ]
b = np.array(a)
print(b)