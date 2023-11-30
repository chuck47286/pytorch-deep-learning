import torch
import torch.nn.functional as F

# 创建两个相似的向量和一个完全不相似的向量
vector_a = torch.tensor([1.0, 2.0, 3.0])
vector_b = torch.tensor([2.0, 4.0, 6.0])  # vector_b 是 vector_a 的倍数
vector_c = torch.tensor([-1.0, -2.0, -9.0])  # vector_c 是 vector_a 的负数

# 计算点积
dot_product_ab = torch.dot(vector_a, vector_b)
dot_product_ac = torch.dot(vector_a, vector_c)

# 计算余弦相似度
cosine_similarity_ab = F.cosine_similarity(vector_a.unsqueeze(0), vector_b.unsqueeze(0))
cosine_similarity_ac = F.cosine_similarity(vector_a.unsqueeze(0), vector_c.unsqueeze(0))

print("Dot product of a and b:", dot_product_ab)
print("Cosine similarity of a and b:", cosine_similarity_ab)
print("Dot product of a and c:", dot_product_ac)
print("Cosine similarity of a and c:", cosine_similarity_ac)