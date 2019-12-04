from series import fibonacci, lucas, sum_series
import pytest

#fib function Test
#first index
def test_one():
  expected = 0
  actual = fibonacci(0)
  assert actual == expected

#second index
def test_two():
  expected = 1
  actual = fibonacci(1)
  assert actual == expected

#third index
def test_three():
  expected = 1
  actual = fibonacci(2)
  assert actual == expected

#twentieth index
def test_four():
  expected = 6765
  actual = fibonacci(20)
  assert actual == expected

#less than 0
def test_five():
  expected = None
  actual = fibonacci(-1)
  assert actual == expected

#failed as expected
def test_six():
  with pytest.raises(TypeError):  # Pass in the expected error
    fibonacci('String')

#lucas function test
#first index
def test_seven():
  expected = 2
  actual = lucas(0)
  assert actual == expected

#second index
def test_eight():
  expected = 1
  actual = lucas(1)
  assert actual == expected

#ninth index
def test_nine():
  expected = 76
  actual = lucas(9)
  assert actual == expected

#failed as expected
def test_ten():
  with pytest.raises(TypeError):
    fibonacci('String')

#sum series function test
#twelve index
def test_eleven():
  expected = 144
  actual = sum_series(12)
  assert actual == expected

