import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
# each row is a student
# each column (col) is a test in the course

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis=0)
# gives us the average for each COLUMN
# in this circumstance, its the avg per test

print("g", g)

numbers = np.array([1, 4, 9, 16, 25, 36])

sqrt = np.sqrt(numbers)

print("sqrt", sqrt)

numbers2 = np.arange(1, 7) * 10

np_add = np.add(numbers, numbers2)

print("addition", np_add)

np_multiply = np.multiply(numbers2, 5)

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

np_multiply2 = np.multiply(numbers3, numbers4)

print("multiply2", np_multiply2)


grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

a = grades[0, 1]
# should be the first row due to index 0
# should be second column due to index 1
print(a)

b = grades[1]
# selects a single row, specify only one index in the brackets
print(b)

c = grades[0:2]
# selects sequential rows (0 through 1) since upper limit is not included
print(c)

d = grades[[1, 3]]
# selects multiple non-sequential rows, use a list of row indices
print(d)

e = grades[:, 0]
# retrieves test 1 for all students
print(e)

# test 1 and test 3 for all students
f = grades[:, [0, 2]]
print(f)

"""
Use NumPy random-number generator to craete an array of 
twelve random grades in the range 60 thru 100, then reshape
the result into a 3-by-4 array. Calculate the avg of all
the grades, the avgs of the grades for each test and the
avgs of the grades for each student. 
"""

randarray = np.array(np.random.randint(60, 100, size=12)).reshape(3, 4)
print(randarray)

avg_all = np.average(randarray)
avg_all = randarray.mean()
print(avg_all)

avg_test = randarray.mean(axis=0)
print(avg_test)

avg_student = randarray.mean(axis=1)
print(avg_student)


""" 
SHALLOW COPIES (VIEW)
"""

numbers = np.arange(1, 6)
print(numbers)
numbers2 = numbers.view()
# reduces space by not making a physical copy of the database
numbers[1] *= 10
print(numbers2)

"""
SLICE VIEWS (Is a shallow copy of array)
"""

numbers2 = numbers2[0:3]

numbers[1] *= 20

print(numbers2)

""" 
DEEP COPY
"""

numbers = np.arange(1, 6)
numbers2 = numbers.copy()
# the array method copy returns a new array object with a deep copy of the original array
numbers[1] *= 10
print(numbers)
print(numbers2)

"""
The array methods of RESHAPE and RESIZE both enable you to change an 
array's dimensions. Method reshape returns a view (shallow copy) of the
original array with new dimensions. It does not modify the original array.
"""
grades = np.array([[87, 96, 70], [100, 87, 90]])
a = grades.reshape(1, 6)

print(grades)

print(a)

b = grades.resize(1, 6)

print(grades)
print(b)


# produces a deep copy
flattened = grades.flatten()
print(flattened)

# produces a shallow copy
raveled = grades.ravel()
print(raveled)

raveled[0] = 100
print(grades)

raveled[5] = 99
print(grades)


t = grades.T
print(t)

print(grades)

grades = np.array([[87, 96, 70], [100, 87, 90]])

grades2 = np.array([[94, 77, 90], [100, 81, 82]])

h_grades = np.hstack((grades, grades2))
print(h_grades)
# adds the two horizontally
# adds more columns


v_grades = np.vstack((grades, grades2))
print(v_grades)
# stacks them vertically
# adds more rows, thus more students