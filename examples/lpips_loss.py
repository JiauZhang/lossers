import torch
from lossers.lpips import LPIPS


loss_fn = LPIPS(net='vgg')
source = torch.randn((1, 3, 32, 32), requires_grad=False)
target = torch.randn((1, 3, 32, 32), requires_grad=True)
optimizer = torch.optim.Adam([target], lr=1e-3, betas=(0.9, 0.999))

for i in range(1000):
    loss = loss_fn(source, target)
    loss = 0
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if i % 10 == 0:
        print('loss info:', loss.item())
