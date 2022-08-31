# numpy

import numpy as np

# create list to np
a = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(a)
print(a)

# Dimension
print(b.ndim)

# row, column
print(b.shape)

# select np's index
print(b[0,0])
print(b[1])
print(b[:2]) # row 0, 1
print(b[[1,2],0])

# increase array
a = np.arange(10)
print(a)
b = np.arange(1,5) # 1 to (5-1)
print(b)

# array zero 0
a = np.zeros((3,3))
print(a)

# array unit 1
a = np.ones((4,3))
print(a)

# designate array's elements
a = np.full((2,3),7)
print(a)

# identity matrix
a = np.eye(4)
print(a)

# dimension transformation
a = np.arange(20)
print(a)
b = a.reshape(4,5)
# b = a.reshape(5,5)
# if reshape's parameter value is different in array's length, error
print(b)

#  slicing
a = np.arange(1,10)
print(a)
b = a.reshape(3,3)
print(b)
c= np.array(b)[0:2,0:2]
print(c)
c= np.array(b)[1:,1:]
print(c)

# calculation
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a+b
print(c)
c = a*b
print(c)
c = a/b
print(c)
arr1 = [[1,2],[3,4]]
arr2 = [[5,6],[7,8]]
a = np.array(arr1)
b = np.array(arr2)
c = np.dot(a,b) # matrix multiplication
# c = arr1*arr2 is error
print(c)
print(np.sum(c)) # sum of all elements
print(np.prod(c)) # multiplication all elements
print(np.mean(c)) # mean
print(np.std(c)) # standard deviation