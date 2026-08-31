#Tests for all code functions 
import pytest
from finance.dcf import cost_of_equity, after_tax_cost_of_debt, wacc, project_revenue 

#cost_of_equity test
def test_cost_of_equity():
    assert cost_of_equity(0.04, 1.2, 0.05) == pytest.approx(0.1)

#after_tax_cost_of_debt test
def test_after_tax_cost_of_debt():
    assert after_tax_cost_of_debt(0.06, 0.25) == pytest.approx(0.045)

#wacc test
def test_wacc():
    assert wacc(0.1, 0.045, 800, 200) == pytest.approx(0.089)

# project_revenue test
def test_project_revenue():
    assert project_revenue(1000, [0.10, 0.08 ]) == pytest.approx([1100.0, 1188.0])