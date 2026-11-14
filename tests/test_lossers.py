import torch
import torch.nn.functional as F

from lossers import math as math_losses
from lossers.clip import clip_loss, contrastive_loss
from lossers.gan import hinge_d_loss, vanilla_d_loss, vanilla_g_loss
from lossers.softmax import AMSoftmax, softmax_loss


def test_softmax_loss_matches_cross_entropy():
    torch.manual_seed(0)
    logits = torch.randn(8, 5)
    labels = torch.randint(0, 5, (8,))

    expected = F.cross_entropy(logits, labels)
    actual = softmax_loss(logits, labels)

    torch.testing.assert_close(actual, expected)


def test_amsoftmax_returns_a_scalar_with_gradients():
    torch.manual_seed(0)
    layer = AMSoftmax(in_dims=16, n_classes=8)
    logits = torch.randn(4, 16)
    labels = torch.tensor([3, 6, 1, 7])

    loss = layer(logits, labels)
    loss.backward()

    assert loss.ndim == 0
    assert torch.isfinite(loss)
    assert layer.weight.grad is not None
    assert layer.weight.grad.shape == layer.weight.shape


def test_contrastive_loss_prefers_the_diagonal():
    torch.manual_seed(0)
    similarity = torch.randn(6, 6) * 4

    loss = contrastive_loss(similarity)

    assert loss.ndim == 0
    assert loss >= 0
    assert loss < F.cross_entropy(similarity, torch.zeros(6, dtype=torch.long))


def test_clip_loss_is_symmetric():
    torch.manual_seed(0)
    similarity = torch.randn(5, 5)

    torch.testing.assert_close(clip_loss(similarity), clip_loss(similarity.t()))


def test_gan_losses():
    real = torch.randn(32)
    fake = torch.randn(32)

    for loss in (hinge_d_loss(real, fake), vanilla_d_loss(real, fake), vanilla_g_loss(fake)):
        assert loss.ndim == 0
        assert torch.isfinite(loss)
        assert loss >= 0

    torch.testing.assert_close(vanilla_g_loss(fake), F.softplus(-fake).mean())


def test_math_aliases_are_callable():
    torch.manual_seed(0)
    prediction = torch.randn(8, 3)
    target = torch.randn(8, 3)

    torch.testing.assert_close(math_losses.l1_loss(prediction, target), F.l1_loss(prediction, target))
    torch.testing.assert_close(math_losses.l2_loss(prediction, target), F.mse_loss(prediction, target))
    torch.testing.assert_close(math_losses.smooth_l1_loss(prediction, target), F.smooth_l1_loss(prediction, target))
