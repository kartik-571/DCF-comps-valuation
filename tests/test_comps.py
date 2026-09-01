# This DCF model was developed with the help of claude AI, and it was mainly used to help with understanding 
# financial terminology, equations and concepts as well as help with reviewing and pointing out potential bugs in code.
# All the code and script was written, and tested by me.

import pytest
from finance.comps import comp_single_calculation, comp_multiple_calculation, rank_comps, filter_comps

#test comp_single_calculation
def test_comp_single_calculation():
    assert comp_single_calculation(company ={"share_price": 25.0, "eps":1.2, "shares_outstanding": 200, "total_debt": 50, "cash_and_cash_equivalents": 30, "ebit": 40, "d_and_a": 10}) == pytest.approx({"pe_ratio":20.83333333 , "ev_ebitda_ratio":100.4 })

#test comp_multiple_calculation
def test_comp_multiple_calculation():
    results = comp_multiple_calculation(companies=[
        {"share_price": 25.0, "eps": 1.2, "shares_outstanding": 200, "total_debt": 50, "cash_and_cash_equivalents": 30, "ebit": 40, "d_and_a": 10},
        {"share_price": 18.0, "eps": 0.9, "shares_outstanding": 150, "total_debt": 20, "cash_and_cash_equivalents": 15, "ebit": 25, "d_and_a": 6},
    ])
    assert results[0] == pytest.approx({"pe_ratio": 20.8333333, "ev_ebitda_ratio": 100.4})
    assert results[1] == pytest.approx({"pe_ratio": 20.0, "ev_ebitda_ratio": 87.25806452})


# test rank_comps
def test_rank_comps():
    companies = [
    {"share_price": 25.0, "eps": 1.2, "shares_outstanding": 200, "total_debt": 50, "cash_and_cash_equivalents": 30, "ebit": 40, "d_and_a": 10},
    {"share_price": 18.0, "eps": 0.9, "shares_outstanding": 150, "total_debt": 20, "cash_and_cash_equivalents": 15, "ebit": 25, "d_and_a": 6},]
    results = comp_multiple_calculation(companies)
    ranked = rank_comps(results, "pe_ratio")
    assert ranked[0] == pytest.approx({'pe_ratio': 20.0, 'ev_ebitda_ratio': 87.25806451612904, 'rank': 1})
    assert ranked[1] == pytest.approx({'pe_ratio': 20.833333333333336, 'ev_ebitda_ratio': 100.4, 'rank': 2})

# test filter_comps
def test_filter_comps():
    companies = [
        {"share_price": 25.0, "eps": 1.2, "shares_outstanding": 200, "total_debt": 50, "cash_and_cash_equivalents": 30, "ebit": 40, "d_and_a": 10},
        {"share_price": 18.0, "eps": 0.9, "shares_outstanding": 150, "total_debt": 20, "cash_and_cash_equivalents": 15, "ebit": 25, "d_and_a": 6},]
    results = comp_multiple_calculation(companies)
    filtered = filter_comps(results, "pe_ratio", 20.5)
    assert filtered[0] == pytest.approx({'pe_ratio': 20.0, 'ev_ebitda_ratio': 87.25806451612904})
    assert len(filtered) == 1
    

    