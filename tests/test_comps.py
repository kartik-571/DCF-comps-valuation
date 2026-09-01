import pytest
from finance.comps import comp_single_calculation

#test comp_single_calculation
def test_comp_single_calculation():
    assert comp_single_calculation(company ={"share_price": 25.0, "eps":1.2, "shares_outstanding": 200, "total_debt": 50, "cash_and_cash_equivalents": 30, "ebit": 40, "d_and_a": 10}) == pytest.approx({"pe_ratio":20.83333333 , "ev_ebitda_ratio":100.4 })