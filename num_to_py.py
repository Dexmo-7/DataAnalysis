import numpy as np

data = np.random.randn(2, 3)
# vector with zeros
data_1 = np.zeros(3)
number = 0

new_data = data * data
# matrix 2x3 multiple by vector 0 equal 0
new_data1 = data * data_1
# matrix 2x3 multiple by 0 equal 0
new_data2 = data * number

matA = np.array([[2, 3, 5], [4, 1, 10]], )
print(matA)
print(matA.dtype)

# fancy indexing
arr = np.empty((8, 4))
for item in range(8):
    arr[item] = item

print(arr)
print("\n")
print(arr[[2, 4, 1, 0]])
print("\n")

arr1 = np.arange().reshape(4, 16)
print(arr1)