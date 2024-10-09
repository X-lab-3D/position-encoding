# POSITION-ENCODING
A library that encodes sequence positions in torch.

## DEPENDENCIES

 * python >= 3.11.5
 * pytorch >= 2.0.1

## INSTALL

Run:

```
python setup.py install
```

## USAGE

Relative position encoding:

```
from position_encoding.relative import get_relative_position_encoding_matrix

# max length of sequence: 16
# encoding depth of each element: 32
m = get_relative_position_encoding_matrix(16, 32)

```

Absolute position encoding:

```
from position_encoding.absolute import get_absolute_position_encoding

# max length of sequence: 16
# encoding depth of each element: 32
e = get_absolute_position_encoding(16, 32)
```
