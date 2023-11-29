import torch

valid_lens = torch.tensor([2, 3])
X = torch.rand(2, 2, 4)

# print(valid_lens)
valid_lens = torch.repeat_interleave(valid_lens, X.shape[1])
# print(valid_lens)

print(torch.normal(0, 1, (2, 1, 20)).shape)
