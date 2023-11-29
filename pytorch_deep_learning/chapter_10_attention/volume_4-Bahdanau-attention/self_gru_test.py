import torch
from torch import nn

# 定义一个简单的 GRU 网络
class SimpleGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleGRU, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers)

    def forward(self, x):
        output, hidden_state = self.gru(x)
        return output, hidden_state

# 网络参数
input_size = 10  # 输入特征的维度
hidden_size = 5  # 隐藏层的维度
num_layers = 2   # GRU层的数量

# 创建网络实例
model = SimpleGRU(input_size, hidden_size, num_layers)

# 创建一些随机输入数据
# 假设序列长度为 3，批次大小为 2
x = torch.randn(3, 2, input_size)
# print(x.shape)
# 通过网络运行输入数据
output, hidden_state = model(x)

# 对最后一层隐藏状态使用 torch.unsqueeze
# hidden_state 的形状为 (num_layers, batch_size, hidden_size)
# 我们获取最后一层，然后增加一个维度
last_hidden_state = torch.unsqueeze(hidden_state[-1], dim=1)

print("Original hidden state shape:", hidden_state.shape)
print("Last hidden state shape after unsqueeze:", last_hidden_state.shape)
print(f'{hidden_state}\n{last_hidden_state}')