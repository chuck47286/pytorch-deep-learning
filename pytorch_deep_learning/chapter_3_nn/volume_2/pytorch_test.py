import torch
import random

true_w = torch.tensor([2, -3.4])
x = torch.tensor([1.0, 1.0, 2.0, 3.0])
# print(f'x.shape {x.shape}, x {x}')
# print(f'x.reshape {x.reshape((-1, 1))}')
# print(f'{true_w}')
# tensor = torch.normal(mean=0, std=1, size=(4, 4))
# print(f'{tensor}')

# 矩阵计算
# matmul = torch.matmul(x, true_w)
# print(f'{matmul}')
#
# matmul += 4.2
# print(f'{matmul}')
# result = x.dot(true_w)
# print(f'{result}')

# print(f'len() {len(true_w)}')
# indices = list(range(5))
# random.shuffle(indices)
# print(f'indices {indices}')

w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
# print(f'{w}')
# print(f'{b}')

print(f'{2 ** 3}')

