#Tests for all code functions 
import pytest
from finance.dcf import cost_of_equity

#cost_of_equity test
def test_cost_of_equity():
    assert cost_of_equity(0.04, 1.2, 0.05) == pytest.approx(0.1)