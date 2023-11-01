import torch


y = torch.tensor([0, 0])
y_hat = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
# print(y_hat[[0, 1], y]) # tensor([0.1000, 0.3000])
# print(y_hat[range(len(y_hat)), y])
# print(y_hat[[0, 1], y])
# print(y_hat[[0, 1], y])  # tensor([0.1000, 0.3000])

# range 用法
# print(f'range(2) {range(2)}, len(y_hat) {len(y_hat)}')
