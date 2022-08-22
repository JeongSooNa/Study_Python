# Character type and Input, Output

## String(문자열)
str = "Hello World"
print(str[2]) # string도 마찬가지로 indexing 가능, immutable
str1 = "Hello","World"
print(str1)
print(str1[1])
str2 = "Hello",777,"World"
print(str2)
print(str2[0])
print(str2[0][1]) # ','가 들어가는 순간 list처럼 indexing된다.
print("Kim's")
print('Kim\'s') # '''을 사용할 때 '\'를 사용!
print("tab : \t, newline : \n wow") # \t : tap, \n : newline
