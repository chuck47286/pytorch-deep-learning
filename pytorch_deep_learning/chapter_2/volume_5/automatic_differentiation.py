import torch

z = torch.ones(4, dtype=torch.float32)
print(f'z {z}')
x = torch.arange(4.0)
x.requires_grad_(True)
print(f'x {x}')
print(x.grad)

y = 2 * torch.dot(x, x)
print(y)

y.backward()
x.grad
print(f'x.grad {x.grad}')

x.grad.zero_()
print(f'x.grad now {x.grad}')
y = x.sum()
print(f'y now {y}')
y.backward()
x.grad
print(f'x.grad {x.grad}')
