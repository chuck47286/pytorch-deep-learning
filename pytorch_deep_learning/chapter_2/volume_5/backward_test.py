import torch

x = torch.arange(4)
y = x * x
print(y)
print(x.grad)
