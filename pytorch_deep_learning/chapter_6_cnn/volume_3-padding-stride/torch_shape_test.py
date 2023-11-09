import torch

X = torch.rand(size=(8, 8))
print(f'x={X} \n X.shape={X.shape}')
# X = X.reshape((1, 1) + X.shape)
# X = X.view(1, 8, 8)
X = X.reshape(1, 8, 8)
print(X)