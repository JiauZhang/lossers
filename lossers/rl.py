import torch
import torch.nn.functional as F


def masked_mean(values: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
    if mask is None:
        return values.mean()
    weights = mask.to(values.dtype)
    return (values * weights).sum() / weights.sum().clamp_min(1)


def ppo_loss(
    logprobs: torch.Tensor,
    old_logprobs: torch.Tensor,
    advantages: torch.Tensor,
    mask: torch.Tensor | None = None,
    clip_range: float = 0.2,
) -> torch.Tensor:
    ratio = torch.exp(logprobs - old_logprobs)
    unclipped = ratio * advantages
    clipped = torch.clamp(ratio, 1 - clip_range, 1 + clip_range) * advantages
    return -masked_mean(torch.minimum(unclipped, clipped), mask)


def grpo_loss(
    logprobs: torch.Tensor,
    old_logprobs: torch.Tensor,
    advantages: torch.Tensor,
    mask: torch.Tensor | None = None,
    clip_range: float = 0.2,
) -> torch.Tensor:
    return ppo_loss(logprobs, old_logprobs, advantages, mask=mask, clip_range=clip_range)


def kl_penalty(
    logprobs: torch.Tensor,
    ref_logprobs: torch.Tensor,
    mask: torch.Tensor | None = None,
) -> torch.Tensor:
    log_ratio = ref_logprobs - logprobs
    return masked_mean(torch.exp(log_ratio) - log_ratio - 1, mask)


def dpo_loss(
    policy_chosen: torch.Tensor,
    policy_rejected: torch.Tensor,
    ref_chosen: torch.Tensor,
    ref_rejected: torch.Tensor,
    beta: float = 0.1,
) -> torch.Tensor:
    margins = beta * ((policy_chosen - policy_rejected) - (ref_chosen - ref_rejected))
    return -F.logsigmoid(margins).mean()
