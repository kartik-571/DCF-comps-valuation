# This DCF model was developed with the help of claude AI, and it was mainly used to help with understanding 
# financial terminology, equations and concepts as well as help with reviewing and pointing out potential bugs in code.
# All the code and script was written, and tested by me.

#Tests for all code functions 
import pytest
from finance.dcf import calculate_dcf, cost_of_equity, after_tax_cost_of_debt, run_dcf_analysis, terminal_value, wacc, project_revenue, calculate_fcf_single_year, project_fcf, sensitivity_analysis

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

#terminal_value test
def test_terminal_value():
    assert terminal_value(100, 0.025, 0.09) == pytest.approx(1576.923076923077)

#second terminal_value test
def test_terminal_value_when_wacc_is_less_than_terminal_growth_rate():
    with pytest.raises(ValueError):
        terminal_value(100, 0.09, 0.05)

# calculate_dcf test
def test_calculate_dcf():
    assert calculate_dcf([100, 100], 0.1) == pytest.approx([90.9090909090909, 82.64462809917356])

#run_dcf_analysis test
def test_run_dcf_analysis():
    assert run_dcf_analysis(0.25, 0.089, 1000, [0.10, 0.08], [0.2, 0.25], [0.03, 0.04], [0.04, 0.05], [0.01, 0.02], 0.025, 200, 100) == pytest.approx({'total_enterprise_value': 3040.86480768428, 'equity_value': 2840.86480768428, 'intrinsic_value_per_share': 28.408648076842802})

def test_sensitivity_analysis():
    table = sensitivity_analysis([0.08, 0.02], [0.02, 0.03], 0.25, 1000, [0.10, 0.08], [0.2, 0.25], [0.03, 0.04], [0.04, 0.05], [0.01, 0.02], 200, 100)
    assert table[0.08][0.02]['intrinsic_value_per_share'] == pytest.approx(30.380740740740734)
    assert table[0.02][0.02] == "Invalid"
