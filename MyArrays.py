import numpy as np

integers = np.array([1, 2, 3])
print(type(integers))

# List Comprehension
# create a 1D array from a list comprehension
# that produces even integers from 2 thru 20

integers = np.array([x for x in range(2, 21, 2)])
print(integers)


# give it TWO square brackets
integers = np.array([[1, 2, 3], [4, 5, 6]])
print(integers)
# each number represents a column, each bracket represents a row

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
print(floats)

a = integers.dtype
b = integers.ndim
c = integers.shape
d = integers.size

print()
"""
for row in integers:
    print(row)
    for col in row:
        print(col, end=" ")
"""
for i in integers.flat:
    print(i)

############
# Exercise #
############

# create a 2 dimensional array of 5 integer elements each using the
# random module and list comprehension print out its dimension,
# shape and size
import random

a = np.array(
    [
        [random.randint(1, 10) for x in range(5)],
        [random.randint(1, 10) for x in range(5)],
    ]
)
# now we will use np random module
b = np.array(np.random.randint(1, 10, size=(2, 5)))
# pcik numbers between 1 and 10, then create a table of
# two rows and five columns
print()

c = np.zeros(5)
# float is the normal data type
d = np.ones(5)
e = np.ones((2, 4), dtype=int)
f = np.full((3, 5), 13)
g = np.arange(5)
h = np.arange(5, 10)
i = np.arange(10, 1, -2)
print()

print(np.linspace(0.0, 1.0, num=5))
# evenly spaced float range
array1 = np.arange(1, 21)
array2 = array1.reshape(4, 5)
print(array1)
print(array2)

array3 = np.arange(1, 100001).reshape(4, 25000)
print(array3)
array4 = np.arange(1, 100001).reshape(100, 1000)
print(array4)

# shows first three and last three rows of an array when highly compact

numbers = np.arange(1, 6)
numbers += 10
print(numbers)
print(numbers * 2)
print(numbers ** 3)
# ^ augmented operation
print(numbers)

# when multiplying integer arrays with floating arrays the result is a floating point
numbers2 = np.linspace(1.1, 5.5, 5)
print(numbers * numbers2)

print(numbers >= 13)
print(numbers2 < numbers)
print(numbers == numbers2)
# both arrays must have the same number of elements
