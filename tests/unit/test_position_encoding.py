import torch

import random

from position_encoding.relative import get_relative_position_encoding_matrix


def test_positional_encoding():

    batch_size = 10
    maxlen = 16

    l=12

    masks = torch.tensor([[i < l for i in range(maxlen)] for _ in range(batch_size)])

    code = get_relative_position_encoding_matrix(maxlen, 32)

    assert torch.all(code[0, 0] == code[5, 5])
    assert torch.all(code[0, 1] == code[5, 6])
    assert torch.all(code[1, 0] == code[6, 5])
    assert torch.any(code[5, 0] != code[0, 5])

    assert torch.any(code[0, 10] != code[2, 5])
