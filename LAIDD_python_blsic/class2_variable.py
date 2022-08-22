# Variable & Assignment

## Test

### 반지름이 5인 원의 면적과 둘레를 계산 하시오.
### 단, 원주율은 3.14
pi = 3.14
r = 5
print("면적 :",r*r*pi)
print("둘레 :",2*r*pi)
# 31.4가 아닌 31.400000000000002 가 나오는 이유?

### 456분은 몇 시간 몇 분인지 계산하시오.
time = 456
print(time//60,"h",time%60,"m")
# int(time/60)으로 자료형을 변환해도 된다.

### 복소수 1+3i와 2+1i의 합을 계산하고, 계산 결과가 3+4i가 맞는지 
### 결정하는 프로그램을 작성하시오.
### 비교 연산법 : a == b
a:complex = 1+3j
b:complex = 2+1j
answer = a+b
print(answer)
if(answer == 3+4j):print("true")
else:print("false")
print(answer == 3+4j)
# = : assign / == : equal