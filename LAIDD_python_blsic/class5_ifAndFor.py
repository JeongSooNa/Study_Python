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
    print(i)
