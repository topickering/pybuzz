from .pybuzz import *
import pytest

def test_pybuzz_one():
    assert pybuzz(1) == '1'

def test_pybuzz_three():
    assert pybuzz(3) == 'Fizz'

def test_pybuzz_six():
    assert pybuzz(6) == 'Fizz'

def test_pybuzz_ten():
    assert pybuzz(10) == 'Buzz'

def test_pybuzz_thirty():
    assert pybuzz(30) == 'FizzBuzz'

def test_is_divisible_by():
    assert divisible_by_x(6, 3) == True

def test_is_not_divisible_by():
    assert divisible_by_x(5, 3) == False
