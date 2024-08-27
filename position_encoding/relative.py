from typing import Optional

import torch


def get_relative_position_encoding_matrix(max_length: int, encoding_depth: Optional[int] = 0) -> torch.Tensor:
    """
    Returns a one-hot encoded relative position matrix. (not masked)
    It distinguishes between left side (.., -2, -1, 0) and right side (0, 1, 2, ..) relative positions.

    Args:
        max_length: max length of the encoded sequence
        encoding_depth: dimensionality for relative position one hot encoding,
                        by default it makes the encoding as large as necessary to fit all relative positions.
    Returns:
        one hot encoded relative positions: [max_length, max_length, encoding_depth]
    """

    min_relpos = 1 - max_length
    max_relpos = max_length - 1

    # [1, 1, r * 2 - 1]
    bins = torch.arange(start=min_relpos, end=max_relpos + 1)[None, None, :]

    if encoding_depth == 0:
        encoding_depth = bins.shape[-1]

    # [max_length]
    r = torch.arange(max_length)

    # [max_length, max_length, 1]
    d = (r[:, None] - r[None, :]).unsqueeze(-1)

    # [max_length, max_length, encoding_depth]
    p = torch.nn.functional.one_hot(
        torch.argmin(torch.abs(d - bins), dim=-1),
        num_classes=encoding_depth,
    )

    return p
