import torch

weights = torch.ones((2, 10)) * 0.1
# print(weights)
# print(weights.unsqueeze(1).shape)

values = torch.arange(20.0).reshape((2, 10))
# print(values)
# print(values.unsqueeze(-1).shape)

n_train = 50  # 训练样本数
x_train, _ = torch.sort(torch.rand(n_train) * 5)   # 排序后的训练样本
print(f'{x_train.shape}\n{x_train}')

n_test = 50  # 测试样本数
keys = x_train.repeat((n_test, 2))
print(f'{keys.shape}\n{keys}')