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

# print(arr)
# print("\n")
# print(arr[[2, 4, 1, 0]])
# print("\n")

# arr1 = np.arange(64).reshape(4, 16)
# print(arr1)

# tabA = np.arange(8).reshape(2, 4)
# tabB = np.random.randn(8).reshape(4, 2)
# tabAtrans = tabA.T
# print(tabA)
# print(tabB)
# print(tabAtrans)

# new_data1 = np.dot(tabAtrans, tabA)

# print("\n")
# print(new_data1)

matA1 = matA.transpose((1, 0))
print(matA1)
print(matA)

# np.where == x if instruction else y
# if in cond will be True then value from xarr, if not value from yarr
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = np.where(cond, xarr, yarr)
print(result, "\n")

# matrix for mean and max methods - matB 3x4
matB = np.array([[10, 4, 2, 5], [4, 2, 1, 1], [3, 2, 7, 9]])
print(matB)
# mean of axis=0 (sum to "up" -> we've got row, in this case we'll obtain 4 values)
# mean of axis=1 (sum to "left" -> we've got column, in this case we'll obtain 3 values)
print("\nMean of matB:\n", np.mean(matB))
print("\nMean of matB axis 0\n", np.mean(matB, axis=0))
print("\nMean of matB axis 1\n", np.mean(matB, axis=1))
