import torch

from lossers.rl import dpo_loss, grpo_loss, kl_penalty, masked_mean, ppo_loss


def test_masked_mean_ignores_masked_entries():
    values = torch.tensor([1.0, 2.0, 3.0])
    mask = torch.tensor([True, False, True])

    torch.testing.assert_close(masked_mean(values, mask), torch.tensor(2.0))


def test_ppo_loss_matches_the_unclipped_objective_at_ratio_one():
    logprobs = torch.tensor([-1.0, -2.0])
    old_logprobs = logprobs.clone()
    advantages = torch.tensor([1.0, -0.5])

    loss = ppo_loss(logprobs, old_logprobs, advantages)

    torch.testing.assert_close(loss, -advantages.mean())


def test_ppo_loss_clips_large_ratios():
    old_logprobs = torch.zeros(1)
    high = ppo_loss(torch.tensor([1.0]), old_logprobs, torch.ones(1), clip_range=0.2)
    low = ppo_loss(torch.tensor([-1.0]), old_logprobs, torch.ones(1) * -1, clip_range=0.2)

    torch.testing.assert_close(high, torch.tensor(-1.2))
    torch.testing.assert_close(low, torch.tensor(0.8))


def test_grpo_loss_uses_the_mask():
    logprobs = torch.tensor([[0.0, 5.0]])
    old_logprobs = torch.zeros(1, 2)
    advantages = torch.tensor([[1.0, 100.0]])
    mask = torch.tensor([[True, False]])

    loss = grpo_loss(logprobs, old_logprobs, advantages, mask=mask)

    torch.testing.assert_close(loss, torch.tensor(-1.0))


def test_kl_penalty_is_zero_for_identical_logprobs():
    logprobs = torch.tensor([-1.0, -2.0])

    torch.testing.assert_close(kl_penalty(logprobs, logprobs), torch.tensor(0.0))


def test_dpo_loss_is_log_two_for_identical_policies():
    chosen = torch.tensor([-1.0])
    rejected = torch.tensor([-2.0])

    loss = dpo_loss(chosen, rejected, chosen, rejected)

    torch.testing.assert_close(loss, torch.log(torch.tensor(2.0)))
