from .pybuzz import *
import pytest

def test_pybuzz_one():
    assert pybuzz(1) == '1'

def test_pybuzz_three():
    assert pybuzz(3) == 'Fizz'
