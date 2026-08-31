#Tests for all code functions 
import pytest
from finance.dcf import cost_of_equity, after_tax_cost_of_debt, wacc, project_revenue, calculate_fcf_single_year, project_fcf

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

#single year FCF calculation test
def test_calculate_fcf_single_year():
    assert calculate_fcf_single_year(0.2, 1000, 0.25, 0.03, 0.04, 0.01) == pytest.approx(130.0)

#project_fcf test
def test_project_fcf():
    assert project_fcf([0.2, 0.25], [1000, 1200], 0.25, [0.03, 0.04], [0.04, 0.05], [0.01, 0.02]) == pytest.approx([130.0, 189.0])