import torch
from torch import nn

net = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 1))
X = torch.rand(size=(2, 4))
print(f'x={X}')
# print(f'X={X} \n {net(X)}')
# 参数访问
# print(net[2].state_dict())
# 目标参数
# print(type(net[2].bias))
# print(net[2].bias)
# print(net[2].bias.data)
# 还没有调用反向传播，所以参数的梯度处于初始状态
# print(f'{net[2].weight.grad == None}')
#
# print(*[(name, param.shape) for name, param in net[0].named_parameters()])
# print(*[(name, param.shape) for name, param in net.named_parameters()])
#
# print(f"{net.state_dict()['2.bias'].data}")

# def block1():
#     return nn.Sequential(nn.Linear(4, 8), nn.ReLU(),
#                          nn.Linear(8, 4), nn.ReLU())
#
# def block2():
#     net = nn.Sequential()
#     for i in range(4):
#         # 在这里嵌套
#         net.add_module(f'block {i}', block1())
#     return net
#
# rgnet = nn.Sequential(block2(), nn.Linear(4, 1))
# print(rgnet)

# def init_normal(m):
#     if type(m) == nn.Linear:
#         nn.init.normal_(m.weight, mean=0, std=0.01)
#         nn.init.zeros_(m.bias)
# net.apply(init_normal)
# print(f'{net[0].weight.data[0], net[0].bias.data[0]}')

# def init_constant(m):
#     if type(m) == nn.Linear:
#         nn.init.constant_(m.weight, 1)
#         nn.init.zeros_(m.bias)
# net.apply(init_constant)
# print(f'{net[0].weight.data[0], net[0].bias.data[0]}')


def init_xavier(m):
    if type(m) == nn.Linear:
        nn.init.xavier_uniform_(m.weight)
def init_42(m):
    if type(m) == nn.Linear:
        nn.init.constant_(m.weight, 42)

net[0].apply(init_xavier)
net[2].apply(init_42)
print(net[0].weight.data[0])
print(net[2].weight.data)