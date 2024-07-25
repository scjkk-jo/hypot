import pytest

import hypot.source as source

# test sqrt function for one scenario
def test_sqrt():
      input = 4
      expected_output = 2.0
      output = source.sqrt(input)
      
      assert output == expected_output
      
# test scenario 2
def test_sqrt1():
      input = 9
      expected_output = 3.0
      output = source.sqrt(input)
      
      assert output == expected_output
      
# test scenario 3
def test_sqrt2():
      input = 0
      expected_output = 0.0
      output = source.sqrt(input)
      
      assert output == expected_output
      
# test hypot function