import torch


def sequence_mask(X, valid_len, value=0):
    """在序列中屏蔽不相关的项"""
    maxlen = X.size(1)
    mask = torch.arange((maxlen), dtype=torch.float32,
                        device=X.device)[None, :] < valid_len[:, None]
    X[~mask] = value
    return X

X = torch.tensor([[1, 2, 3], [4, 5, 6]])
# print(sequence_mask(X, torch.tensor([1, 3])))

arrange = torch.arange((6), dtype=torch.float32, device=X.device)
# tensor1 = torch.tensor([0, 4])
tensor2 = torch.tensor([1, 4])

# mask = tensor1 < tensor2
# print(mask)

none_1 = arrange[None, :]
none_2 = arrange[:, None]
# none_3 = arrange[:, :]
# print(f'{none_1}\n{none_2}\n{None}')
print(f'{none_1.shape}\n{none_2.shape}\n{None}')


tensor_none_1 = tensor2[None, :]
tensor_none_2 = tensor2[:, None]
# print(f'{tensor_none_1}\n{tensor_none_2}\n{None}')
print(f'{tensor_none_1.shape}\n{tensor_none_2.shape}\n{None}')

none__1 = none_1 < tensor_none_2
# none__2 = none_2 < tensor_none_2  # error non-singleton dimension
print(f'{none__1}\n{None}')

# tensor_none__1 = none_1 < tensor_none_1  # error non-singleton dimension
tensor_none__2 = none_2 < tensor_none_1
print(f'{None}\n{tensor_none__2}')