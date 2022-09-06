# os package

import os

print("***")

# current directory
print(os.getcwd())

# ls
print(os.listdir())
desk = os.listdir('/Users/IDC-Monitor-PC/Desktop')
print(desk)
# Get .txt using for
for i in desk :
    if i.endswith('.txt') :
        print(i)

