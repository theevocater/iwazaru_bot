from collections import OrderedDict

from shared import limited_dict


def test_limit():
    d = limited_dict.LimitedSizeDict({1: 2, 3: 4, 5: 6}, size_limit=1)
    assert len(d) == 1
    d[3] = 4
    assert len(d) == 1


def test_no_limit():
    keys = range(1, 1000)
    d = limited_dict.LimitedSizeDict.fromkeys(keys)
    assert len(d) == len(keys)
    for a, b in zip(d, OrderedDict.fromkeys(keys)):
        assert a == b
