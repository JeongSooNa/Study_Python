# If and For

## Boolean logic
## false : false, 0, None, [], (), {}
## true : false를 제외한 모두. (-1도 true)
a = 1
b = 1
print(a==b)
print(a is b)
print(id(a))
print(id(b)) # 값이 작을 때는 같은 주소를 공유한다.
print((1,2,3,4) < (1,2,4))
print((1,2)<(1,2,-1))
## == : 값을 비교 / is : 주소는 비교

## If statement
## if elif else
x = int(input("x = "))
if 1 < x < 5 :
    print("in range")
else :
    print("out of range")
x = int(input("x = "))
if 1 < x <= 5 :
    print("lower range")
elif 5 < x <= 10 :
    print("higher range")
else :
    print("out of range")
y = 1/x if x > 0 else 0 # 조건에 따라 값을 할당
print(y)

## for statement
for i in range(10) :
    print(i) # 0부터 9(10개)까지
for i in range(10,0,-1) :
    print(i) # 10~1까지 -1 감소하면서
for i in "mystring" :
    print(i) # 문자열 한 글자씩 출력
for i in ["red","blue","green"] :
    print(i)

## for문을 이용한 구구단 생성
for i in range(2,10) :
    print("[{0:d}단]".format(i))
    for j in range(1,10) :
        tmp = i*j
        print("{0:d} * {1:d} = {2:d}".format(i,j,tmp))
    print("---")
v = list(range(10))
print(v)
print([i for i in v]) # One-line for문

## continue & break
for i in range(1,10) :
    if 2 <= i <= 5 :
        continue
    print(i)
for i in range(1,10) :
    if i == 5 :
        break
    print(i)

## While statement
i = 0
while i < 10 :
    print(i)
    i += 1
i = 0
while 1 :
    print(i)
    i += 1
    if i >= 10 :
        break

## references
a1 = 10
a2 = a1
a1 = 50
print(a1,a2) # 변수에 값을 할당
b1 = [10]
b2 = b1
b1[0] = 50
print(b1,b2) # list, dictionary는 값이 아닌 주소를 할당하기 때문에 주소가 같아 동일한 값이 나온다.
c1 = [10]
c2 = c1[:] # c1이 아닌 c1의 값을 할당하여 주소가 아닌 값이 할당.
c1[0] = 50
print(c1,c2)

## TEST
## 국어, 영어, 수학 점수를 입력 받아서 평균을 계산하고 평균에 따라 등급을 부여하는 프로그램을 작성 하시오.
## ex) 국어:90 / 영어:85 / 수학:72 , 평균은 82.3이며, 등급은 B입니다.
kor = float(input("korean : "))
eng = float(input("English : "))
math = float(input("Mathmatics : "))
avg = (kor+eng+math)/3
grade = ""
if avg >= 90 :
    grade = "A"
elif avg >=80 :
    grade = "B"
elif avg >=70 :
    grade = "C"
elif avg >=60 :
    grade = "D"
else :
    grade = "F"
print("평균은 {0:.1f}점 이며, 등급은 {1:s}입니다.".format(avg,grade))

## 라인 수를 입력 받아서 아래와 같은 모양을 출력하는 프로그램을 작성하시오.
## line:11 / 
# 10000000001
# 01000000010
# 00100000100
#    ....
# 10000000001
line = int(input("please input line : "))
for i in range(0,line) :
    tmp = ""
    for j in range(0,line) :
        if i == j :
            tmp += "1"
        elif (line-i-1) == j :
            tmp += "1"
        else :
            tmp += "0"
    print(tmp)

## 반복문과 조건문을 사용하여 입력된 정수들 중에서 가장 큰 값을 출력하는 프로그램을 작성하시오.
## ex) Numbers : 10,456,87,78 / Max : 456
max = 0
numbers = []
while 1 :
    numbers = numbers + [int(input("please input numbers : "))]
    flag = input("Are you keep input?(y/n) : ")
    if flag == "y" :
        continue
    else :
        break
print(numbers)
for i in numbers :
    if max < i :
        max = i
print("max : {0:d}".format(max))
## 강의에서는 한번에 input 받고 split으로 나누었다.