# Character type and Input, Output

## String(문자열)
import json
import string


str0 = "Hello World"
print(str0[2]) # string도 마찬가지로 indexing 가능, immutable
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
print("""this is 
    justhis""") # multiple lines (tab 가능)
print("str1"+"   "+"str2") # ','말고 '+'를 사용하면 문자열 합성
print("a"*3) # 반복

## formatting
## "{index:type} string {index:yupe}...".format(parameter,parameter...)
## s : 문자열 / d : 10진수 정수 / f : 부동소수, ...
str0 = "{0:s}={1:.3f} meters or {2:d} cm".format("height",1.0,100) # format으로 mapping해준다.
print(str0)

## Indexing, Slicing
str0 = "This is Justhis"
print(str0[3])
print(str0[3:8])
print(len(str0)) # return length

## 형 변환
a = str(3.14); print(a)
b = float("3.14"); print(b)
c = int("3"); print(c)

## String Method
str0 = "  Hello World  "
print(str0.upper()) # 대문자 변환
print(str0.lower()) # 소문자 변환
print(str0.count("l")) # 문자열 내 문자 count
print(str0.index("l")) # 문자열 내 문자 index(없으면 error)
print(str0.join("***")) # 문자 사이에 문자열 삽입
print(str0.lstrip()) # 왼쪽 공백 제거
print(str0.rstrip()) # 오른쪽 공백 제거
print(str0.strip()) # 양쪽 공백 제거
print(str0.replace(" ","")) # 특정 문자 replace
print(str0.split("l")) # 특정 문자로 나누어 list
print(str0.swapcase()) # 대.소문자 바꾸기

## Input
## input(prompt)
name = input("What's your name? : ")
age = input("How old are you? : ")
print("name : "+name+"\nage : "+age)
print("You have ",65-int(age),"years until retirement.") # age를 받아오면서 int로 변환해도 됨.

## output
print("Hello World")
age = 29
print("You have ",65-age,"years until retirement.")

## TEST
## x값을 입력 받아 다음 2차 방정식의 y값을 계산하는 프로그램을 작성하시오.
## 방정식 : y = 3x^2 + 5x + 3
## input : x = 2.1 / output : y = 26.73
x = float(input("x = "))
y = 3*x*x+5.0*x+3.0
print("y={0:.2f}".format(y))

## 반지름을 입력 받아 원의 둘레와 넓이를 구하는 프로그램을 작성하시오.
## 원주율 : 3.14 / input : r = 1 / output : 반지름 1.0인 원의 넓이는 3.1이고 둘레는 6.3입니다.
r = float(input("r = "))
pi = 3.14
a = pi*r*r
c = 2*pi*r
print("반지름이 {0:.1f}인 원의 넓이는 {1:.1f}이고 둘레는 {2:.1f}입니다.".format(r,a,c))

## 아래 문자열을 대상으로 지정된 기능을 수행하는 프로그램을 작성하시오.
## 문자열 양쪽의 공백을 제거
## "나"를 "너"로 변환
str0 = """ 죽는 날까지 하늘을 우러러
한 점 부끄럼이 없기를,
잎새에 이는 바람에도
나는 괴로워했다.
별을 노래하는 마음으로
모든 죽어가는 것을 사랑해야지
그리고 나한테 주어진 길을
걸어가야겠다.
오늘 밤에도 별이 바람에 스치운다.    """
str0 = str0.strip()
str0 = str0.replace("나","너")
print("[별 헤는 밤]")
print(str0)

