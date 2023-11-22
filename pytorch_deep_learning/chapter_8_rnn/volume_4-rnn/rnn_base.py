import torch
from d2l import torch as d2l

X, W_xh = torch.normal(0, 1, (3, 1)), torch.normal(0, 1, (1, 4))
H, W_hh = torch.normal(0, 1, (3, 4)), torch.normal(0, 1, (4, 4))
# print(f'X={X}\nW_xh={W_xh}\nH={H}\nW_hh={W_hh}')
xh_ = torch.matmul(X, W_xh)
hh_ = torch.matmul(H, W_hh)
print(f'XH_={xh_}\nhh_={hh_}')
print(xh_ + hh_)

matmul = torch.matmul(torch.cat((X, H), 1), torch.cat((W_xh, W_hh), 0))
print(matmul)

