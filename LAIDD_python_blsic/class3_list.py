# structured data type

## list
### list slicing
from audioop import avg


nums = [2,4,6,8,10]
### indexing
print(nums[0])
### reverse indexing
print(nums[-2]) # 리스트의 index 역순으로도 지정 가능.
### print all
print(nums[:]) # 시작과 끝이 지정되지 않아 모 출력
### 1부터 (3-1)까지
print(nums[1:3])
### 2칸씩 띄워서 출력
print(nums[::2])
### 처음부터 [-1]까지 출력
print(nums[:-1])
### [-3]부터 끝까지 출력
print(nums[-3:])
### 1씩 줄여가면서 출력 (뒤집기)
print(nums[::-1])

### 응용
print("** plus traing")
nums2 = [1,2,3,4,5,6,7,8,9,10]
print(nums2[2:8:2]) # 3,5,7
print(4 in nums)
print(5 in nums)
nums3 = nums + [1,3] # list 추가
print(nums3)
nums4 = nums * 2 # list 반복
print(nums4)
nums2[0] = 0 # list mutable
print(nums2)
nums2[1], nums2[2] = 0, 0 # python만 갖고있는 특이한 구조
print(nums2)
print(sum(nums)) # 합 (기본 내장 함수)
print(max(nums)) # 최댓값
print(min(nums)) # 최솟값
nums5 = range(5) # nums를 출력하면 range로 나오고, index를 출력하면 확인 가능
for i in nums5 : print(i)

### list method
a = [0,2,4,6]
a.append(1); print(a) # list 추가
a.sort(); print(a) # list sort (문자도 abc순, 문자보다 숫자가 먼저 온다.1)
a.sort(reverse=True); print(a) # list sort(내림차순)
a.reverse(); print(a) # list 순서 거꾸로
print(a.index(4)) # list 값의 index return
a.insert(3,5); print(a) # list의 index에 값 insert(insert index 뒤의 값은 뒤로 밀린다.)
a.remove(2); print(a) # list에서 처음 나오는 값 삭제
print(a.pop()); print(a) # list의 마지막 요소 return 후 삭제
print(a.count(1)) # list안에 값이 몇개 있는지 return
b = [1,2,3]
a.extend(b); print(a) # list에 list를 더하기
a.append(b); print(a) # extend와 append의 차이점!

## tuple (튜플)
### list와 유사하지만 immutable한 자료
tup = ()
tup = (1,2,3)
colors = ("red","green","blue")
print(tup[1])
print(colors[1])
print(tup[1:3])

## dictionary (딕셔너리)
### key & value (JSON과 동일 구조)
dic = {"name":"js", "age":29, "gender":"m"}
print(dic)
dic = dict(name="js", age=29, gender="m")
print(dic)
dic = dict([("name","js"),("age",29),("gender","m")]) # tuple형식
print(dic)
print(dic["name"])
print(dic["age"])
dic["age"] = 30 # mutable
print(dic["age"])
dic["company"] = "syntekabio"
print(dic)
dic[(1,2)] = "tuple"
print(dic) # key와 value는 list, tuple, 다른 dictionary가 될 수 있다.

### dictionary method
print(dic.keys()) # dictionary의 key return
print(dic.values()) # dictionary의 value return
print(dic.items()) # dictionary의 tuple return
print(dic.get("name")) # dictionary key의 해당 value
print(dic.get("home")) # key가 없어 none return
# dic.clear(); print(dic) # dictionary 초기화

dic1 = list(dic); print(dic1) # key list
dic2 = list(dic.keys()); print(dic2) # key list
dic3 = list(dic.values()); print(dic3) # value list
dic4 = list(dic.items()); print(dic4) # tuple(key,value) list

## Test
### 아래의 list 내용을 역순으로 출력
nums = [1,2,3,4,5]
strs = ["abc","def","ghi"]
print(nums[::-1])
print(strs[::-1])
nums.reverse()
strs.reverse()
print(nums)
print(strs)

### 학점 data를 dictionary에 저장 후 이름순으로 첫번째 학생의 학점을 출력
### 홍길동 : 3.4, 임꺽정 : 4.0, 김철수 : 2.8, 이영희 : 3.9
students = {
    "홍길동" : 3.4,
    "임꺽정" : 4.0,
    "김철수" : 2.8,
    "이영희" : 3.9
    }
stu_list = list(students.keys())
stu_list.sort()
print(stu_list)
result = students.get(stu_list[0])
print(result) # 다음 code를 풀어쓰느냐는 style!
