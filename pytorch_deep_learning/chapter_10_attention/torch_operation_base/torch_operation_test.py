import torch

a = torch.tensor([[1,2],[3,4]])
b = torch.tensor([[5,6],[7,8]])
a_b = a * b    # Hadamard product
t = a @ b      # matrix multiplication
print(f'{a_b}\n{t}')


