import torch

A = torch.randn(3, 2, 2, 4)
B = torch.randn(3, 2, 4, 5)

C = torch.randn(3, 4)
D = torch.randn(4, 5)

matmul = torch.matmul(A, B)
# print(matmul.shape)

torch_matmul = torch.matmul(C, D)
mm = torch.mm(C, D)
# print(torch_matmul)
# print(mm)
# print(f'torch.eq(torch_matmul, mm)={torch.eq(torch_matmul, mm)}'
#       f'\n'
#       f'torch.allclose(torch_matmul, mm)={torch.allclose(torch_matmul, mm)}'
#       f'\n'
#       f'torch.equal(torch_matmul, mm)={torch.equal(torch_matmul, mm)}')

list1 = [1,2,3,4,5]
print(list1)
list2 = list(range(5))
tensor_list = [torch.tensor([num]) for num in list2 ]
print(list2)
print(tensor_list)

cat = torch.cat(tensor_list, dim=0)
print(cat)
