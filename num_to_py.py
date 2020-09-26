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

print(data)
print(data_1)
print(new_data)
print(new_data1)
print(new_data2)
