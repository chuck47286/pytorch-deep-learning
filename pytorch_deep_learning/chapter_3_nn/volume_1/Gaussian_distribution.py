import matplotlib.pyplot as plt
import math
import time
import numpy as np
import torch
from d2l import torch as d2l

from chapter_3_nn.volume_1.Timer import Timer

n = 10000
a = torch.ones([n])
b = torch.ones([n])

print(a)
print(b)

# 直接计算两个向量的+运算 （0.15496 sec）
c = torch.zeros(n)
timer = Timer()
for i in range(n):
    c[i] = a[i] + b[i]
print(f'{timer.stop():.5f} sec, {c}')

# 其他方式  矢量化代码通常会带来数量级的加速 （0.00000 sec）
timer.start()
d = a + b
print(f'{timer.stop():.5f} sec, {d}')

# 高斯分布
def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma**2)
    return p * np.exp(-0.5 / sigma**2 * (x - mu)**2)

# 再次使用numpy进行可视化
x = np.arange(-7, 7, 0.01)

# 均值和标准差对
params = [(0, 1), (0, 2), (3, 1)]
d2l.plot(x, [normal(x, mu, sigma) for mu, sigma in params], xlabel='x',
         ylabel='p(x)', figsize=(4.5, 2.5),
         legend=[f'mean {mu}, std {sigma}' for mu, sigma in params])
plt.show() # 显示图形