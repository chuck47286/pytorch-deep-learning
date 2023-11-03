import torch

x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
print(f'{x} {len(x)}')

like = torch.ones_like(x)
print(f'{like} {len(like)}')

y = torch.relu(x)
y.backward(torch.ones_like(x), retain_graph=True)
print(f'{y}')

