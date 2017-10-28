import pytest
import binary as b

def test_binary_init_int():
    binary = b.Binary(6)
    assert int(binary) == 6


def test_binary_init_binstr():
    binary = b.Binary('0b110')
    assert int(binary) == 6


def test_binary_init_hexstr():
    binary = b.Binary('0x6')
    assert int(binary) == 6


def test_binary_init_hex():
    binary = b.Binary(0x6)
    assert int(binary) == 6


def test_binary_init_intseq():
    binary = b.Binary([1,1,0])
    assert int(binary) == 6


def test_binary_init_strseq():
    binary = b.Binary(['1', '1', '0'])
    assert int(binary) == 6


def test_binary_init_negative():
    with pytest.raises(ValueError):
        binary = b.Binary(-4)


def test_binary_str():
    binary = b.Binary(6)
    assert str(binary) == '110'


