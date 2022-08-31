# The Last Letter

# input first value
first_value = input("Please input your first word : ")
last_letter = first_value[len(first_value)-1]

# TLL Logic
while True :
    value = input("Please input your word : ")
    if value[0] == last_letter :
        print("next..")
        last_letter = value[len(value)-1]
        continue
    else :
        print("fail..")
        break