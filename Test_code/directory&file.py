import os


## basic
## CRUD directory and files

## get current directory path(pwd)
a = os.getcwd()
print(a)



os.chdir('../../')

## create file and write
file = open("./test.txt",'w')
file.write("Hello world!")
file.close()

## append text in file
file = open("./test.txt",'a')
file.write("\nMy name is JS")
file.close()

## read by line
file = open("./test.txt",'r')
for line in file :
    print(line)


## return to current directory
os.chdir(a)