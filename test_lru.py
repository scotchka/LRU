import pytest
from lru import LRU, Node


def test_node():
    assert Node([1, 2, 3]) == Node([1, 2, 3])
    assert Node('a') != Node('b')
    assert repr(Node('a')) == "Node('a')"


def test_cache():
    d = LRU(3)

    d['1'] = 1
    d['2'] = 2
    d['3'] = 3

    assert d == {'1': 1, '2': 2, '3': 3}

    d['1'] = 1

    d['4'] = 4

    assert d['4'] == 4

    assert d == {'3': 3, '1': 1, '4': 4}

    assert list(d) == ['4', '1', '3']

    assert list(reversed(d)) == ['3', '1', '4']


def test_exceptions():
    d = LRU(1)

    d['a'] = 1

    assert len(d) == 1

    assert d == {'a': 1}

    with pytest.raises(NotImplementedError):
        del d['a']

    with pytest.raises(NotImplementedError):
        d.pop('a')
