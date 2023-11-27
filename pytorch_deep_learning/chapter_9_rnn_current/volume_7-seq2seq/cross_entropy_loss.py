import torch
from torch.nn import functional as F

def cross_entropy_loss(y_true, y_pred):
    # y_true 是标签的索引，y_pred 是预测的原始得分（未应用 softmax）
    m = y_pred.shape[0]
    p = F.softmax(y_pred, dim=1)
    log_likelihood = -torch.log(p[range(m), y_true])
    loss = torch.mean(log_likelihood)
    return loss

# test 示例
# y_true = torch.tensor([2, 0, 1, 2])
# y_pred = torch.tensor([[0.1, 0.2, 0.7], [1.0, 0.2, 0.3], [0.2, 0.2, 0.6], [0.4, 0.4, 0.6]])
# loss = cross_entropy_loss(y_true, y_pred)
# print(loss)
