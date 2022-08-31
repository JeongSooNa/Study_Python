# numpy

import numpy

# create list to numpy
a = [[1,2,3],[4,5,6],[7,8,9]]
b = numpy.array(a)
print(a)

# Dimension
print(b.ndim)

# row, column
print(b.shape)

# select numpy's index
print(b[0,0])
print(b[1])
print(b[:2]) # row 0, 1
print(b[[1,2],0])

# increase array
a = numpy.arange(10)
print(a)
b = numpy.arange(1,5) # 1 to (5-1)
print(b)

# array zero 0
a = numpy.zeros((3,3))
print(a)

# array unit 1
a = numpy.ones((4,3))
print(a)

# designate array's elements
a = numpy.full((2,3),7)
print(a)

# identity matrix
a = numpy.eye(4)
print(a)

# dimension transformation
a = numpy.arange(20)
print(a)
b = a.reshape(4,5)
# b = a.reshape(5,5)
# if reshape's parameter value is different in array's length, error
print(b)

#  slicing
a = numpy.arange(1,10)
print(a)
b = a.reshape(3,3)
print(b)
c= numpy.array(b)[0:2,0:2]
print(c)
c= numpy.array(b)[1:,1:]
print(c)

# calculation
