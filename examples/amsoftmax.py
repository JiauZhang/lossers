import torch
from lossers.softmax import AMSoftmax

batch, in_dims, n_classes = 2, 16, 8
ams = AMSoftmax(in_dims, n_classes)
logits = torch.randn(batch, in_dims)
labels = torch.tensor([3, 6]).view(batch)

print(ams.forward(logits, labels))
