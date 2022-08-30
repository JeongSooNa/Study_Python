# Caculate StandardError
import math

def se(list) :
        result = 0
        n = len(list)
        m = sum(list) / n
        l1 = []
        l2 = []
        for i in list :
                l1.append(i - m)
        for i in l1 :
                l2.append(i*i)
        return sum(l2)/(n-1)
list = [1.0, 2.0, 3.0, 4.0, 5.0]
print(se(list)) 
# 2.5

## Please check parameter's type
## ex) float, int, string
