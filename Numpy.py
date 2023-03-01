import numpy as np
import time
# array = np.array([1,2,3,4,5])

# print(type(array))


revenues = [2000, 5000, 3000, 65000, 7200, 31000, 26550, 1900, 3840, 5100, 41000]

initial_time = time.time()

sum = 0

for i in revenues:

    sum +=i

# print(sum)

termination_time = time.time()

# print("Executeion Time: ",termination_time-initial_time)

array = np.array(revenues)

initial_time = time.time()

sum = array.sum()

# print(sum)

termination_time = time.time()

# print("Execution Time: ",termination_time-initial_time)


x = ['Ben',500,'Jake','Liz',6000]
print(x)

for i in x:
    print(type(i))


arrayx = np.array(x)
print(arrayx)

for i in arrayx:
    print(type(i))



array2 = np.array([[1,2,3],[4,5,6]])

# print(array2)

array2.ndim
2
array2.shape
3
array2.size
6