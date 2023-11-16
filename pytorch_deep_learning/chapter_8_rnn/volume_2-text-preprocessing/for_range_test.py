import torch
# for 循环写法
a = 0
b = 3
# 遍历范围
# for i in range(a, a + b):
#     print(i)
#
# for i in range(a, a + b, 2):
#     print(i)

# 遍历列表
# for element in [1, 2, 5, 4]:
#     print(element)

# 创建一维张量
tensor_1d = torch.tensor((1,2,3,4,5,7), dtype=torch.float32)
print(tensor_1d)

tensor_2d = tensor_1d.reshape((2,3))
print(tensor_2d)

tensor_2d = tensor_1d.reshape((3, -1))
print(tensor_2d)

rand = torch.rand(2)
print(rand)
tensor_2d[1,:] = rand
print(tensor_2d)