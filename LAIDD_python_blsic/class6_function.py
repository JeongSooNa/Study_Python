# Function

## basic structure
def function_name(arg1,arg2):
    return arg1+arg2
f1 = function_name(1,2)
f2 = function_name("Hello"," World")
f3 = function_name([1,2],[3,4])
print(f1)
print(f2)
print(f3)


## sum function
def sum_function1(list):
    return sum(list)
def sum_function2(list):
    result = 0
    for i in list:
        result += i
    return result
list = [1,2,3,4,5]
print(sum_function1(list))
print(sum_function2(list))

## default parameter
def sum_1(x = 1, y = 2):
    return x+y
print(sum_1())
print(sum_1(3)) # parameter가 여러 개 일때, 갯수가 달라도 순서대로 입력된다.
print(sum_1(3,3))
print(sum_1(y=1))

## variable argument
def f1(c,*args):
    return c*sum(args)
print(f1(2,1,2,3)) # 2*(1+2+3)으로 tuple로 parameter를 받는다.

def f2(*args):
    return(args)
print(f2(1,2,3))

def f3(*args,**kargs):
    c = kargs.get("scale")
    o = kargs.get("offset")
    return o+c*sum(args)
print(f3(1,2,3,scale=2,offset=0))

def f4(**kargs):
    print(kargs)
f4(name="JeongSooNa",age=29,job="developer")

## import
## 실행 시 상단에 import, from 등으로 외부 함수를 불러와야 사용 가능.
import math
x = math.sin(3.14)
print(x)

from math import sin
print(sin(3.14))
print(math.cos(3.14))

from math import sin, cos
print(sin(3.14))
print(cos(3.14))

from math import * # 모든 method 사용 가능(주의!)(다른 module의 method와 충돌 가능)
print(sin(3.14))
print(cos(3.14))

import math as m # alias
print(m.sin(3.14))
print(m.cos(3.14))

## math library
x = -11.4
y = 10.5
print(max(x,y)) # 최댓값
print(min(x,y)) # 최솟값
print(abs(x), math.fabs(x)) # 절댓값, abs()라는 내장 함수 존재.
print(math.ceil(x)) # 올림
print(math.floor(x)) # 내림
print(round(x)) # 반올림
print(math.e) # e
print(math.pi) # 원주율
print(math.log(y)) # log
print(math.log10(y)) # log10
print(math.sin(x)) # sin
print(math.cos(x)) # cos
print(math.sqrt(y)) # root

## module
## 다른 python program에서 import하여 쓸 수 있게 만들어진 file
## function, class, variable 등이 내장.
## 같은 directory에 있는 file 사용.
import class6_function_module as mod
x = 5
y = 10
## 현재 사용자가 main인가?(직접 module을 실행시켰다면 True, 다른 file에서 import하면 False return)
def main():
    print(mod.sum_function(x,y))
if __name__ == "__main__":
    main() # import한 module의 print는 실행x / 현재 사용자가 실행하는 print만 적용.

## TEST
## 입력 받은 문자열을 다음과 같은 방법으로 암호화하고 복호화하는 프로그램을 작성하시오.
## 암호화(Encryption) : 공백(space,tap)으로 분리, 역순으로 배치, ascii code를 key만큼 증가.
## 복호화(Decryption) : ascii code를 key만큼 감소, 공백(space,tap)으로 분리, 역순으로 배치
## ex) key:1 / "abc def" > 암호화 > "efg!bcd" > 복호화 > "abc def"
## ord(x) : 문자를 ascii code로 변환
## chr(x) : ascii code를 문자로 변환
key = 1
str = "abc def"
def asc(str,key): # 문자열을 ascii code로 key만큼 증가시켜 변환하는 함수
    result = ""
    for i in str:
        code = ord(i)
        result += chr(code+key)
    return result
def enc(str,key): # 암호화 함수
    list = str.split() # 공백 분리
    list = list[::-1] # reverse
    result = " ".join(list) # 합성
    return asc(result,key) # 뒤집은 문자열을 ascii code로 key만큼 바꿔 return
def dec(str,key): # 복호화 함수
    result = asc(str,key*-1) # 문자열을 -key만큼 ascii code로 변환
    list = result.split() # 공백 분리
    list = list[::-1] # reverse
    result = " ".join(list) # 합성
    return result

encode = enc(str,key)
print(encode) # 암호화
print(dec(encode,key)) # 복호화


## n명의 이름과 전화번호를 입력 받아 전화번호 사전을 만들고, 이름과 전화번호로 검색하는 프로그램을 작성하시오.
