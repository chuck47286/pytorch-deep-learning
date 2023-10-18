import matplotlib.pyplot as plt
import torch
from torch.distributions import multinomial
import d2l.torch as d2l

fair_probs = torch.ones([6]) / 6
# one_sample = multinomial.Multinomial(1, fair_probs).sample()
# print(one_sample)

# ten_sample = multinomial.Multinomial(10, fair_probs).sample()
# print(ten_sample)


# 将结果存储为32位浮点数以进行除法
# counts = multinomial.Multinomial(1000, fair_probs).sample()
# counts / 1000  # 相对频率作为估计值
# print(counts)

# 10次取样 500组
counts = multinomial.Multinomial(10, fair_probs).sample((500,))
# 按照横轴dim=0 逐行累加数据
cum_counts = counts.cumsum(dim=0)
# 按照纵轴dim=1 计算当前数据在这一向量中的分布大小
estimates = cum_counts / cum_counts.sum(dim=1, keepdims=True)
print(counts)
print(cum_counts)
print(estimates)

d2l.set_figsize((6, 4.5))
for i in range(6):
    plt.plot(estimates[:, i].numpy(),
             label=("P(die=" + str(i + 1) + ")"))
plt.axhline(y=0.167, color='black', linestyle='dashed')
plt.gca().set_xlabel('Groups of experiments')
plt.gca().set_ylabel('Estimated probability')
plt.legend()

plt.show() # 显示图形